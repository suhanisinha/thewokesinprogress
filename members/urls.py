from django.urls import path
from .views import MemberRegisterView, SettingsView, PasswordChangeViews, ProfilePageView

urlpatterns = [
    path('register/', MemberRegisterView.as_view(), name='register'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('password/', PasswordChangeViews.as_view(), name='password-change'),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),
]
