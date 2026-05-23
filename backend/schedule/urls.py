from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('faculties', views.FacultyViewSet)
router.register('departments', views.DepartmentViewSet)
router.register('groups', views.StudentGroupViewSet)
router.register('teachers', views.TeacherViewSet)
router.register('subjects', views.SubjectViewSet)
router.register('classrooms', views.ClassroomViewSet)
router.register('time-slots', views.TimeSlotViewSet)
router.register('semesters', views.SemesterViewSet)
router.register('schedule', views.ScheduleEntryViewSet, basename='schedule')
router.register('changes', views.ScheduleChangeViewSet, basename='changes')
router.register('audit', views.AuditLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]