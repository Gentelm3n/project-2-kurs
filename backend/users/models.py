from django.conf import settings
from django.db import models


class StaffProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='staff_profile',
        verbose_name='Пользователь',
    )
    faculty = models.ForeignKey(
        'schedule.Faculty',
        on_delete=models.CASCADE,
        related_name='staff_members',
        verbose_name='Факультет',
    )
    position = models.CharField(
        'Должность',
        max_length=100,
        blank=True,
        help_text='Например: "Заместитель декана", "Диспетчер"',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Профиль сотрудника'
        verbose_name_plural = 'Профили сотрудников'

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} — {self.faculty.short_name}"