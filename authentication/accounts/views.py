from django.contrib.auth import views
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import logout

from .models import User
from .forms import ChangeUserForm, RegistrationUserForm


def index(request):
    return render(request, 'accounts/index.html')


class LoginUserView(LoginView):
    template_name = 'accounts/login.html'


class RegistrationUserView(CreateView):
    model = User
    template_name = 'accounts/registration.html'
    form_class = RegistrationUserForm
    success_url = reverse_lazy('accounts:login')


class LogoutUserView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/index.html'


class ChangeUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/change_user.html'
    form_class = ChangeUserForm
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(User, pk=self.request.user.pk)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/delete_user.html'
    success_url = reverse_lazy('accounts:index')

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(User, pk=self.request.user.pk)


def profile(request):
    return render(request, 'accounts/profile.html')
