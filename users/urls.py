from django.urls import path
from .views import RegisterView, ProfileView, VerifyEmailView,LoginView, RequestPasswordResetView, VerifyResetTokenView, ResetPasswordView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/<uuid:token>/', VerifyEmailView.as_view()),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password/reset/request/', RequestPasswordResetView.as_view()),
    path('password/reset/verify/<uuid:token>/', VerifyResetTokenView.as_view()),
    path('password/reset/', ResetPasswordView.as_view()),

]
