
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/',views.LogoutUserView.as_view() ,name='logout'),
    path('registration/', views.RegistrationUserView.as_view(), name='registration'),
    path('profile/', views.profile, name='profile'),
    path('profile/delete/', views.DeleteUserView.as_view(), name='delete'),
    path('profile/change/', views.ChangeUserView.as_view(), name='change_user')
   
]
