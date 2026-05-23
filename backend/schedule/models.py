from django.conf import settings
from django.db import models
from django.utils import timezone


# СПРАВОЧНИКИ

class Faculty(models.Model):
    name = models.CharField('Название', max_length=255)
    short_name = models.CharField('Сокращение', max_length=50)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'
        ordering = ['short_name']

    def __str__(self):
        return self.short_name


class Department(models.Model):
    name = models.CharField('Название', max_length=255)
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name='departments',
        verbose_name='Факультет',
    )

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'
        ordering = ['name']

    def __str__(self):
        return self.name


class StudentGroup(models.Model):
    name = models.CharField('Название группы', max_length=50, unique=True)
    course = models.PositiveSmallIntegerField('Курс')
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='groups',
        verbose_name='Кафедра',
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Teacher(models.Model):
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True,
        related_name='teachers', verbose_name='Кафедра',
    )
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ['last_name', 'first_name']

    @property
    def full_name(self):
        parts = [self.last_name, self.first_name, self.middle_name]
        return ' '.join(p for p in parts if p)

    def __str__(self):
        middle_initial = f'{self.middle_name[0]}.' if self.middle_name else ''
        return f'{self.last_name} {self.first_name[0]}.{middle_initial}'


class Subject(models.Model):
    name = models.CharField('Название', max_length=255)
    short_name = models.CharField('Сокращение', max_length=50, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True,
        related_name='subjects', verbose_name='Кафедра',
    )

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'
        ordering = ['name']

    def __str__(self):
        return self.short_name or self.name


class Classroom(models.Model):
    class RoomType(models.TextChoices):
        LECTURE = 'lecture', 'Лекционная'
        LAB = 'lab', 'Лабораторная'
        SEMINAR = 'seminar', 'Семинарская'

    number = models.CharField('Номер', max_length=20)
    building = models.CharField('Корпус', max_length=100)
    capacity = models.PositiveIntegerField('Вместимость', null=True, blank=True)
    room_type = models.CharField(
        'Тип', max_length=50,
        choices=RoomType.choices, default=RoomType.LECTURE,
    )

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'
        constraints = [
            models.UniqueConstraint(fields=['number', 'building'], name='unique_classroom')
        ]
        ordering = ['building', 'number']

    @property
    def display_name(self):
        return f'{self.building}, ауд. {self.number}'

    def __str__(self):
        return self.display_name


class TimeSlot(models.Model):
    slot_number = models.PositiveSmallIntegerField('Номер пары', unique=True)
    start_time = models.TimeField('Начало')
    end_time = models.TimeField('Конец')

    class Meta:
        verbose_name = 'Временной слот'
        verbose_name_plural = 'Временные слоты'
        ordering = ['slot_number']

    def __str__(self):
        return f'{self.slot_number} пара ({self.start_time:%H:%M}–{self.end_time:%H:%M})'


class Semester(models.Model):
    name = models.CharField('Название', max_length=100)
    start_date = models.DateField('Начало')
    end_date = models.DateField('Конец')
    is_active = models.BooleanField('Активный', default=False)

    class Meta:
        verbose_name = 'Семестр'
        verbose_name_plural = 'Семестры'
        ordering = ['-start_date']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Гарантируем, что только один семестр может быть активным
        if self.is_active:
            Semester.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


# РАСПИСАНИЕ

class ScheduleEntry(models.Model):
    class LessonType(models.TextChoices):
        LECTURE = 'lecture', 'Лекция'
        SEMINAR = 'seminar', 'Семинар'
        LAB = 'lab', 'Лабораторная'

    class WeekType(models.TextChoices):
        EVERY = 'every', 'Каждую неделю'
        ODD = 'odd', 'Верхняя'
        EVEN = 'even', 'Нижняя'

    DAY_CHOICES = [
        (1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'),
        (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье'),
    ]

    semester = models.ForeignKey(
        Semester, on_delete=models.CASCADE, related_name='entries',
        verbose_name='Семестр',
    )
    group = models.ForeignKey(
        StudentGroup, on_delete=models.CASCADE, related_name='schedule',
        verbose_name='Группа',
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name='Дисциплина',
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель',
    )
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, verbose_name='Аудитория',
    )
    time_slot = models.ForeignKey(
        TimeSlot, on_delete=models.CASCADE, verbose_name='Пара',
    )
    day_of_week = models.PositiveSmallIntegerField(
        'День недели', choices=DAY_CHOICES,
    )
    lesson_type = models.CharField(
        'Тип занятия', max_length=20,
        choices=LessonType.choices, default=LessonType.LECTURE,
    )
    week_type = models.CharField(
        'Тип недели', max_length=20,
        choices=WeekType.choices, default=WeekType.EVERY,
    )

    # Soft delete
    is_active = models.BooleanField('Активна', default=True)
    deleted_at = models.DateTimeField('Удалена', null=True, blank=True)
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='deleted_entries',
        verbose_name='Кем удалена',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Запись расписания'
        verbose_name_plural = 'Записи расписания'
        ordering = ['day_of_week', 'time_slot__slot_number']
        constraints = [
            # Преподаватель не может быть в двух местах одновременно
            models.UniqueConstraint(
                fields=['semester', 'teacher', 'day_of_week', 'time_slot', 'week_type'],
                condition=models.Q(is_active=True),
                name='unique_teacher_slot',
            ),
            # Аудитория не может быть занята дважды
            models.UniqueConstraint(
                fields=['semester', 'classroom', 'day_of_week', 'time_slot', 'week_type'],
                condition=models.Q(is_active=True),
                name='unique_classroom_slot',
            ),
            # Группа не может быть в двух местах одновременно
            models.UniqueConstraint(
                fields=['semester', 'group', 'day_of_week', 'time_slot', 'week_type'],
                condition=models.Q(is_active=True),
                name='unique_group_slot',
            ),
        ]

    @property
    def day_name(self):
        return dict(self.DAY_CHOICES).get(self.day_of_week, '')

    def __str__(self):
        return f'{self.day_name} | {self.time_slot} | {self.subject} | {self.group}'


class ScheduleChange(models.Model):
    """Замены и отмены конкретных занятий на конкретную дату."""
    original_entry = models.ForeignKey(
        ScheduleEntry, on_delete=models.CASCADE, related_name='changes',
        verbose_name='Исходная запись',
    )
    change_date = models.DateField('Дата замены')
    new_subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Новая дисциплина',
    )
    new_teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Новый преподаватель',
    )
    new_classroom = models.ForeignKey(
        Classroom, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Новая аудитория',
    )
    new_time_slot = models.ForeignKey(
        TimeSlot, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Новое время',
    )
    is_cancelled = models.BooleanField('Отменено', default=False)
    reason = models.TextField('Причина', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Замена'
        verbose_name_plural = 'Замены'
        ordering = ['-change_date']
        # Нельзя создать две замены для одной записи на одну дату
        constraints = [
            models.UniqueConstraint(
                fields=['original_entry', 'change_date'],
                name='unique_change_per_entry_per_date',
            ),
        ]

    def __str__(self):
        status = 'ОТМЕНА' if self.is_cancelled else 'ЗАМЕНА'
        return f'{status} {self.change_date} — {self.original_entry}'


# АУДИТ

class AuditLog(models.Model):
    """Журнал всех изменений в расписании."""

    class ActionType(models.TextChoices):
        CREATE = 'create', 'Создание'
        UPDATE = 'update', 'Изменение'
        DELETE = 'delete', 'Удаление'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, verbose_name='Пользователь',
    )
    action = models.CharField('Действие', max_length=10, choices=ActionType.choices)
    model_name = models.CharField('Модель', max_length=100)
    object_id = models.BigIntegerField('ID объекта')
    old_data = models.JSONField('Старые данные', null=True, blank=True)
    new_data = models.JSONField('Новые данные', null=True, blank=True)
    ip_address = models.GenericIPAddressField('IP-адрес', null=True)
    timestamp = models.DateTimeField('Время', auto_now_add=True)

    class Meta:
        verbose_name = 'Запись аудита'
        verbose_name_plural = 'Журнал аудита'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['-timestamp']),
            models.Index(fields=['user', '-timestamp']),
            models.Index(fields=['model_name', 'object_id']),
        ]

    def __str__(self):
        action_display = self.get_action_display() or self.action or '?'
        user_str = self.user if self.user_id else 'Неизвестно/Удален'
        return f'[{action_display}] {self.model_name} #{self.object_id} — {user_str}'