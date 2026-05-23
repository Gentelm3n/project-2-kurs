from django.utils import timezone
from rest_framework import serializers
from .models import (
    Faculty, Department, StudentGroup, Teacher,
    Subject, Classroom, TimeSlot, Semester,
    ScheduleEntry, ScheduleChange, AuditLog,
)


class FacultyPermissionMixin:
    """Миксин для проверки прав сотрудника на редактирование факультета."""

    context: dict
    def _check_faculty_permission(self, faculty_id):
        request = self.context.get('request')
        # Если запроса нет или юзер не авторизован - пропускаем
        if not request or not request.user.is_authenticated:
            return

        if request.user.is_superuser:
            return

        staff_profile = getattr(request.user, 'staff_profile', None)
        if not staff_profile:
            raise serializers.ValidationError("У вас нет профиля сотрудника.")

        if staff_profile.faculty_id != faculty_id:
            raise serializers.ValidationError("Вы не можете изменять расписание чужого факультета.")



# СПРАВОЧНИКИ

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    faculty_name = serializers.CharField(source='faculty.short_name', read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'faculty', 'faculty_name']


class StudentGroupSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)
    faculty_name = serializers.CharField(
        source='department.faculty.short_name', read_only=True,
    )

    class Meta:
        model = StudentGroup
        fields = ['id', 'name', 'course', 'department', 'department_name', 'faculty_name']


class TeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Teacher
        fields = [
            'id', 'last_name', 'first_name', 'middle_name',
            'department', 'email', 'phone', 'full_name',
        ]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class ClassroomSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(read_only=True)

    class Meta:
        model = Classroom
        fields = ['id', 'number', 'building', 'capacity', 'room_type', 'display_name']


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'


# РАСПИСАНИЕ — ЧТЕНИЕ (для мобильного приложения)

class ScheduleEntryReadSerializer(serializers.ModelSerializer):
    group = StudentGroupSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)
    classroom = ClassroomSerializer(read_only=True)
    time_slot = TimeSlotSerializer(read_only=True)
    day_name = serializers.CharField(read_only=True)
    lesson_type_display = serializers.CharField(
        source='get_lesson_type_display', read_only=True,
    )
    week_type_display = serializers.CharField(
        source='get_week_type_display', read_only=True,
    )

    class Meta:
        model = ScheduleEntry
        fields = [
            'id', 'semester', 'group', 'subject', 'teacher',
            'classroom', 'time_slot', 'day_of_week', 'day_name',
            'lesson_type', 'lesson_type_display',
            'week_type', 'week_type_display',
            'is_active', 'updated_at',
        ]


# РАСПИСАНИЕ — ЗАПИСЬ (для desktop-приложения деканата)

class ScheduleEntryWriteSerializer(FacultyPermissionMixin, serializers.ModelSerializer):

    day_of_week = serializers.IntegerField(min_value=1, max_value=7)

    class Meta:
        model = ScheduleEntry
        fields = [
            'id', 'semester', 'group', 'subject', 'teacher',
            'classroom', 'time_slot', 'day_of_week',
            'lesson_type', 'week_type', 'is_active',
        ]

    def validate_group(self, value):
        """Проверка прав: нельзя создавать расписание для чужого факультета."""
        self._check_faculty_permission(value.department.faculty_id)
        return value

    def validate_semester(self, value):
        """Нельзя добавлять новые записи в неактивный семестр."""
        # Проверяем только при создании нового объекта ИЛИ при смене семестра
        if not self.instance or getattr(self.instance, 'semester', None) != value:
            if not value.is_active:
                raise serializers.ValidationError(
                    'Нельзя добавлять записи в неактивный семестр.'
                )
        return value

    def validate(self, data):
        """Проверка конфликтов: преподаватель, аудитория, группа. Поддерживает PATCH."""
        # Безопасное извлечение полей: берем из data, если нет - из self.instance (при PATCH)
        semester = data.get('semester', getattr(self.instance, 'semester', None))
        teacher = data.get('teacher', getattr(self.instance, 'teacher', None))
        classroom = data.get('classroom', getattr(self.instance, 'classroom', None))
        group = data.get('group', getattr(self.instance, 'group', None))
        day = data.get('day_of_week', getattr(self.instance, 'day_of_week', None))
        slot = data.get('time_slot', getattr(self.instance, 'time_slot', None))
        week = data.get('week_type', getattr(self.instance, 'week_type', 'every'))

        # активные записи в том же семестре, день, пара
        qs = ScheduleEntry.objects.filter(
            semester=semester,
            day_of_week=day,
            time_slot=slot,
            is_active=True,
        )

        # Исключаем текущий объект при обновлении
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        # Определяем, какие week_type конфликтуют
        if week == 'every':
            conflicting_qs = qs
        elif week == 'odd':
            conflicting_qs = qs.filter(week_type__in=['every', 'odd'])
        else:  # even
            conflicting_qs = qs.filter(week_type__in=['every', 'even'])

        # Конфликт преподавателя
        if conflicting_qs.filter(teacher=teacher).exists():
            raise serializers.ValidationError({'teacher': 'Преподаватель уже занят в это время.'})

        # Конфликт аудитории
        if conflicting_qs.filter(classroom=classroom).exists():
            raise serializers.ValidationError({'classroom': 'Аудитория уже занята в это время.'})

        # Конфликт группы
        if conflicting_qs.filter(group=group).exists():
            raise serializers.ValidationError({'group': 'У группы уже есть занятие в это время.'})

        return data


# ЗАМЕНЫ
class ScheduleChangeReadSerializer(serializers.ModelSerializer):
    """Развёрнутый формат замены для мобильного приложения."""
    original_entry = ScheduleEntryReadSerializer(read_only=True)
    new_subject = SubjectSerializer(read_only=True)
    new_teacher = TeacherSerializer(read_only=True)
    new_classroom = ClassroomSerializer(read_only=True)
    new_time_slot = TimeSlotSerializer(read_only=True)

    class Meta:
        model = ScheduleChange
        fields = '__all__'


class ScheduleChangeWriteSerializer(FacultyPermissionMixin, serializers.ModelSerializer):
    """Компактный формат замены для desktop-приложения."""

    class Meta:
        model = ScheduleChange
        fields = '__all__'

    def validate_original_entry(self, value):
        """Проверка прав: нельзя делать замены для чужого факультета."""
        self._check_faculty_permission(value.group.department.faculty_id)
        return value

    def validate_change_date(self, value):
        """Нельзя создать замену на прошедшую дату."""
        # Разрешаем сохранять прошедшую дату, если мы просто редактируем старую замену (PATCH)
        if not self.instance or getattr(self.instance, 'change_date', None) != value:
            if value < timezone.now().date():
                raise serializers.ValidationError('Нельзя создать замену на прошедшую дату.')
        return value

    def validate(self, data):
        """Базовая проверка конфликтов для замен."""
        change_date = data.get('change_date', getattr(self.instance, 'change_date', None))
        new_time_slot = data.get('new_time_slot', getattr(self.instance, 'new_time_slot', None))
        new_teacher = data.get('new_teacher', getattr(self.instance, 'new_teacher', None))
        new_classroom = data.get('new_classroom', getattr(self.instance, 'new_classroom', None))
        is_cancelled = data.get('is_cancelled', getattr(self.instance, 'is_cancelled', False))

        # Если пару не отменяют, а переносят в другое время/аудиторию/к другому преподу:
        if not is_cancelled and new_time_slot:
            qs = ScheduleChange.objects.filter(
                change_date=change_date,
                new_time_slot=new_time_slot,
                is_cancelled=False
            )
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)

            # Проверяем, не назначена ли на эту же дату и время другая замена с тем же преподом/аудиторией
            if new_teacher and qs.filter(new_teacher=new_teacher).exists():
                raise serializers.ValidationError(
                    {'new_teacher': 'Этот преподаватель уже ведет другую пару (по замене) в это время.'})
            if new_classroom and qs.filter(new_classroom=new_classroom).exists():
                raise serializers.ValidationError(
                    {'new_classroom': 'Эта аудитория уже занята (по замене) в это время.'})

        return data


# АУДИТ

class AuditLogSerializer(serializers.ModelSerializer):
    user_display = serializers.SerializerMethodField()
    action_display = serializers.CharField(source='get_action_display', read_only=True)

    class Meta:
        model = AuditLog
        fields = [
            'id', 'user', 'user_display', 'action', 'action_display',
            'model_name', 'object_id', 'old_data', 'new_data',
            'ip_address', 'timestamp',
        ]
        read_only_fields = fields

    def get_user_display(self, obj):
        if obj.user:
            return obj.user.get_full_name() or obj.user.username
        return 'Система'