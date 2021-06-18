from django.urls import path, include

from .views import CreateAccount, ConfirmAccount, LoginUser, ChangePassword, MyProfileDashboard

urlpatterns = [
    path('register/', CreateAccount.as_view(), name='register'),
    path('confirm-account/', ConfirmAccount.as_view(), name='confirm-account'),
    path('login/', LoginUser.as_view(), name='login-user'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('dashboard/', MyProfileDashboard.as_view(), name='dashboard')
]