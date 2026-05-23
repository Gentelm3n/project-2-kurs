from django.contrib import admin
from .models import StaffProfile


@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'faculty', 'position', 'created_at')
    list_filter = ('faculty',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'faculty__name')

    list_select_related = ('user', 'faculty')

    autocomplete_fields = ('user', 'faculty')