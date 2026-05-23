from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import (
    Faculty, Department, StudentGroup, Teacher,
    Subject, Classroom, TimeSlot, Semester,
    ScheduleEntry, ScheduleChange, AuditLog,
)
from .serializers import (
    FacultySerializer, DepartmentSerializer, StudentGroupSerializer,
    TeacherSerializer, SubjectSerializer, ClassroomSerializer,
    TimeSlotSerializer, SemesterSerializer,
    ScheduleEntryReadSerializer, ScheduleEntryWriteSerializer,
    ScheduleChangeReadSerializer, ScheduleChangeWriteSerializer,
    AuditLogSerializer,
)
from .permissions import IsStaffOrReadOnly, IsOwnFacultyOrReadOnly, IsAuditReadOnly
from .mixins import AuditMixin


# СПРАВОЧНИКИ (CRUD с аудитом)

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ['name', 'short_name']


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.select_related('faculty').all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsStaffOrReadOnly]
    filterset_fields = ['faculty']
    search_fields = ['name']


class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentGroup.objects.select_related(
        'department', 'department__faculty',
    ).all()
    serializer_class = StudentGroupSerializer
    permission_classes = [IsStaffOrReadOnly]
    filterset_fields = ['course', 'department', 'department__faculty']
    search_fields = ['name']


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related('department').all()
    serializer_class = TeacherSerializer
    permission_classes = [IsStaffOrReadOnly]
    filterset_fields = ['department', 'department__faculty']
    search_fields = ['last_name', 'first_name']


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.select_related('department').all()
    serializer_class = SubjectSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ['name', 'short_name']


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsStaffOrReadOnly]
    filterset_fields = ['building', 'room_type']
    search_fields = ['number', 'building']


class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    permission_classes = [IsStaffOrReadOnly]


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsStaffOrReadOnly]

    @action(detail=False, methods=['get'])
    def active(self, request):
        """Возвращает текущий активный семестр."""
        semester = Semester.objects.filter(is_active=True).first()
        if semester:
            serializer = SemesterSerializer(semester, context=self.get_serializer_context())
            return Response(serializer.data)
        return Response(
            {'detail': 'Нет активного семестра.'},
            status=status.HTTP_404_NOT_FOUND,
        )



# РАСПИСАНИЕ (основной ViewSet с аудитом и защитой)

class ScheduleEntryViewSet(AuditMixin, viewsets.ModelViewSet):
    permission_classes = [IsOwnFacultyOrReadOnly]
    filterset_fields = [
        'semester', 'group', 'teacher', 'day_of_week',
        'week_type', 'lesson_type',
    ]

    def get_queryset(self):
        return (
            ScheduleEntry.objects
            .select_related(
                'group', 'group__department', 'group__department__faculty',
                'subject', 'teacher', 'classroom', 'time_slot', 'semester',
            )
            .filter(is_active=True)
            .order_by('day_of_week', 'time_slot__slot_number')
        )

    def get_serializer_class(self):
        # Добавлены кастомные экшены для корректной генерации документации (Swagger/OpenAPI)
        if self.action in ('list', 'retrieve', 'by_group', 'by_teacher', 'by_classroom'):
            return ScheduleEntryReadSerializer
        return ScheduleEntryWriteSerializer

    @action(detail=False, methods=['get'], url_path=r'by-group/(?P<group_id>[0-9]+)')
    def by_group(self, request, group_id=None):
        """
        Расписание для конкретной группы в активном семестре.
        Основной эндпоинт для мобильного приложения.
        """
        get_object_or_404(StudentGroup, pk=group_id)

        entries = self.get_queryset().filter(
            group_id=group_id,
            semester__is_active=True,
        )

        page = self.paginate_queryset(entries)
        if page is not None:
            serializer = ScheduleEntryReadSerializer(page, many=True, context=self.get_serializer_context())
            return self.get_paginated_response(serializer.data)

        serializer = ScheduleEntryReadSerializer(entries, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'by-teacher/(?P<teacher_id>[0-9]+)')
    def by_teacher(self, request, teacher_id=None):
        """Расписание для конкретного преподавателя."""
        get_object_or_404(Teacher, pk=teacher_id)

        entries = self.get_queryset().filter(
            teacher_id=teacher_id,
            semester__is_active=True,
        )

        page = self.paginate_queryset(entries)
        if page is not None:
            serializer = ScheduleEntryReadSerializer(page, many=True, context=self.get_serializer_context())
            return self.get_paginated_response(serializer.data)

        serializer = ScheduleEntryReadSerializer(entries, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'by-classroom/(?P<classroom_id>[0-9]+)')
    def by_classroom(self, request, classroom_id=None):
        """Расписание аудитории — какие занятия проходят в конкретном кабинете."""
        get_object_or_404(Classroom, pk=classroom_id)

        entries = self.get_queryset().filter(
            classroom_id=classroom_id,
            semester__is_active=True,
        )

        page = self.paginate_queryset(entries)
        if page is not None:
            serializer = ScheduleEntryReadSerializer(page, many=True, context=self.get_serializer_context())
            return self.get_paginated_response(serializer.data)

        serializer = ScheduleEntryReadSerializer(entries, many=True, context=self.get_serializer_context())
        return Response(serializer.data)


# ЗАМЕНЫ

class ScheduleChangeViewSet(AuditMixin, viewsets.ModelViewSet):
    permission_classes = [IsOwnFacultyOrReadOnly]
    filterset_fields = ['change_date', 'original_entry__group', 'is_cancelled']

    def get_queryset(self):
        return (
            ScheduleChange.objects
            .select_related(
                'original_entry', 'original_entry__group',
                'original_entry__subject', 'original_entry__teacher',
                'original_entry__classroom', 'original_entry__time_slot',
                'new_subject', 'new_teacher', 'new_classroom', 'new_time_slot',
            )
            # Не отдаем замены для мягко удаленных пар основного расписания
            .filter(original_entry__is_active=True)
            .order_by('-change_date')
        )

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve', 'today', 'by_group_date'):
            return ScheduleChangeReadSerializer
        return ScheduleChangeWriteSerializer

    @action(detail=False, methods=['get'])
    def today(self, request):
        """Все замены на сегодня."""
        changes = self.get_queryset().filter(change_date=timezone.now().date())

        page = self.paginate_queryset(changes)
        if page is not None:
            serializer = ScheduleChangeReadSerializer(page, many=True, context=self.get_serializer_context())
            return self.get_paginated_response(serializer.data)

        serializer = ScheduleChangeReadSerializer(changes, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

    @action(
        detail=False, methods=['get'],
        url_path=r'by-group/(?P<group_id>[0-9]+)/(?P<date>\d{4}-\d{2}-\d{2})',
    )
    def by_group_date(self, request, group_id=None, date=None):
        """Замены для конкретной группы на конкретную дату."""
        get_object_or_404(StudentGroup, pk=group_id)

        changes = self.get_queryset().filter(
            original_entry__group_id=group_id,
            change_date=date,
        )
        # Так как тут нет пагинации (обычно замен 1-2 штуки), можно отдавать сразу
        serializer = ScheduleChangeReadSerializer(changes, many=True, context=self.get_serializer_context())
        return Response(serializer.data)


# АУДИТ (только чтение)

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Журнал аудита — только чтение, только для сотрудников.
    Записи создаются автоматически через AuditMixin.
    """
    queryset = AuditLog.objects.select_related('user').all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAuditReadOnly]
    filterset_fields = ['action', 'model_name', 'user']
    search_fields = ['model_name']