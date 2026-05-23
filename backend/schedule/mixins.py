import logging
from django.utils import timezone
from .models import AuditLog

logger = logging.getLogger(__name__)


class AuditMixin:

    def _get_client_ip(self, request):
        # Оставляем как было, если уверены в настройках Nginx
        xff = request.META.get('HTTP_X_FORWARDED_FOR')
        if xff:
            return xff.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')

    def _serialize_for_audit(self, instance):
        try:
            return self.get_serializer(instance).data
        except Exception:
            return {'id': getattr(instance, 'pk', None), 'str': str(instance)}

    def _get_user(self):
        user = self.request.user
        return user if user.is_authenticated else None

    def perform_create(self, serializer):
        instance = serializer.save()
        try:
            AuditLog.objects.create(
                user=self._get_user(),
                action=AuditLog.ActionType.CREATE,
                model_name=instance.__class__.__name__,
                object_id=instance.pk,
                new_data=serializer.data,
                ip_address=self._get_client_ip(self.request),
            )
        except Exception:
            logger.exception('Ошибка записи аудита (create)')

    def perform_update(self, serializer):
        # Берем старые данные ДО сохранения, не делая лишний запрос в БД
        old_data = self._serialize_for_audit(serializer.instance)

        updated = serializer.save()

        try:
            AuditLog.objects.create(
                user=self._get_user(),
                action=AuditLog.ActionType.UPDATE,
                model_name=updated.__class__.__name__,
                object_id=updated.pk,
                old_data=old_data,
                new_data=serializer.data,
                ip_address=self._get_client_ip(self.request),
            )
        except Exception:
            logger.exception('Ошибка записи аудита (update)')

    def perform_destroy(self, instance):
        # Сначала собираем старые данные
        old_data = self._serialize_for_audit(instance)
        model_name = instance.__class__.__name__
        obj_id = instance.pk

        # Выполняем удаление (soft delete или обычное)
        if hasattr(instance, 'deleted_at'):
            instance.is_active = False
            instance.deleted_at = timezone.now()
            instance.deleted_by = self._get_user()
            instance.save(update_fields=['is_active', 'deleted_at', 'deleted_by'])
        else:
            instance.delete()

        # если удаление прошло успешно, пишем лог
        try:
            AuditLog.objects.create(
                user=self._get_user(),
                action=AuditLog.ActionType.DELETE,
                model_name=model_name,
                object_id=obj_id,
                old_data=old_data,
                ip_address=self._get_client_ip(self.request),
            )
        except Exception:
            logger.exception('Ошибка записи аудита (delete)')