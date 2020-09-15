from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.urls import reverse_lazy
from .forms import RegisterForm, SettingsForm, PasswordChangeForms
from django.contrib.messages.views import SuccessMessageMixin
from blog.models import Profile

class MemberRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class SettingsView(generic.UpdateView):
    form_class = SettingsForm
    template_name = 'registration/settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordChangeViews(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForms
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('settings')
    success_message = 'Your password was changed successfully.'


class ProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        profile_page = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['profile_page'] = profile_page
        return context