from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserSerializer
from .throttles import LoginRateThrottle


class ThrottledTokenObtainPairView(TokenObtainPairView):
    """Получение JWT-токена с rate limiting."""
    throttle_classes = [LoginRateThrottle]


class ThrottledTokenRefreshView(TokenRefreshView):
    """Обновление JWT-токена с rate limiting."""
    throttle_classes = [LoginRateThrottle]


class CurrentUserView(generics.RetrieveAPIView):
    """Возвращает данные текущего авторизованного пользователя."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user