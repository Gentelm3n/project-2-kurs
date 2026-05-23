from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    """
    GET, HEAD, OPTIONS — доступно всем (студенты читают расписание).
    POST, PUT, PATCH, DELETE — только сотрудникам деканата (is_staff=True).
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and
                    (request.user.is_staff or request.user.is_superuser))


class IsOwnFacultyOrReadOnly(BasePermission):
    """
    Сотрудник деканата может редактировать расписание (PUT/PATCH/DELETE)
    только своего факультета. Суперпользователь — любого.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and
                    (request.user.is_staff or request.user.is_superuser))

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True

        staff_profile = getattr(request.user, 'staff_profile', None)
        if staff_profile is None:
            return False

        # Определяем факультет объекта
        entry_faculty_id = self._get_faculty_id(obj)
        if entry_faculty_id is None:
            return False

        return staff_profile.faculty_id == entry_faculty_id

    def _get_faculty_id(self, obj):
        """Извлекает ID факультета из объекта расписания."""
        # ScheduleEntry → group → department → faculty
        if hasattr(obj, 'group'):
            return obj.group.department.faculty_id
        # ScheduleChange → original_entry → group → department → faculty
        if hasattr(obj, 'original_entry'):
            return obj.original_entry.group.department.faculty_id
        return None


class IsAuditReadOnly(BasePermission):
    """Аудит-лог: только чтение, только для сотрудников."""

    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            return False
        return bool(request.user and request.user.is_authenticated and
                    (request.user.is_staff or request.user.is_superuser))