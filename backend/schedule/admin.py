from django.contrib import admin
from .models import (
    Faculty, Department, StudentGroup, Teacher,
    Subject, Classroom, TimeSlot, Semester,
    ScheduleEntry, ScheduleChange, AuditLog,
)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'name')
    search_fields = ('name', 'short_name')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')
    list_filter = ('faculty',)
    search_fields = ('name',)
    list_select_related = ('faculty',)


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'department')
    list_filter = ('course', 'department__faculty')
    search_fields = ('name',)
    list_select_related = ('department',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'department', 'email')
    list_filter = ('department__faculty', 'department')
    search_fields = ('last_name', 'first_name')
    list_select_related = ('department',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'department')
    list_filter = ('department',)
    search_fields = ('name', 'short_name')
    list_select_related = ('department',)


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('number', 'building', 'room_type', 'capacity')
    list_filter = ('building', 'room_type')
    search_fields = ('number', 'building')  # Добавлено для autocomplete_fields


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('slot_number', 'start_time', 'end_time')
    ordering = ('slot_number',)


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active',)


@admin.register(ScheduleEntry)
class ScheduleEntryAdmin(admin.ModelAdmin):
    list_display = (
        'group', 'day_of_week', 'time_slot', 'subject',
        'teacher', 'classroom', 'lesson_type', 'week_type', 'is_active',
    )
    list_filter = ('semester', 'group', 'day_of_week', 'is_active', 'lesson_type')
    search_fields = ('subject__name', 'teacher__last_name', 'group__name')

    # Явная подгрузка связей для быстрого отображения списка
    list_select_related = ('group', 'time_slot', 'subject', 'teacher', 'classroom', 'semester')

    # autocomplete_fields удобнее чем raw_id_fields (появится красивый поиск с лупой)
    autocomplete_fields = ('group', 'subject', 'teacher', 'classroom')


@admin.register(ScheduleChange)
class ScheduleChangeAdmin(admin.ModelAdmin):
    list_display = ('original_entry', 'change_date', 'is_cancelled', 'reason')
    list_filter = ('is_cancelled', 'change_date')
    date_hierarchy = 'change_date'

    list_select_related = (
        'original_entry__time_slot',
        'original_entry__subject',
        'original_entry__group',
        'original_entry__teacher',
    )

    raw_id_fields = ('original_entry',)
    autocomplete_fields = ('new_subject', 'new_teacher', 'new_classroom')


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'action', 'model_name', 'object_id', 'ip_address')
    list_filter = ('action', 'model_name')
    date_hierarchy = 'timestamp'
    list_select_related = ('user',)  # Оптимизация ForeignKey пользователя

    readonly_fields = (
        'user', 'action', 'model_name', 'object_id',
        'old_data', 'new_data', 'ip_address', 'timestamp',
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False