from django.urls import path
from . import views

urlpatterns = [
    path('token/', views.ThrottledTokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', views.ThrottledTokenRefreshView.as_view(), name='token_refresh'),
    path('me/', views.CurrentUserView.as_view(), name='current_user'),
]