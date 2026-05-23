from rest_framework.throttling import AnonRateThrottle


class LoginRateThrottle(AnonRateThrottle):
    """
    Жёсткий лимит на попытки входа: 5 попыток в минуту на один IP.
    Защита от brute force атак на эндпоинт получения JWT-токена.
    """
    rate = '5/minute'

    def get_cache_key(self, request, view):
        return self.cache_format % {
            'scope': 'login',
            'ident': self.get_ident(request),
        }