from django.urls import path
from .views import IndexView, BaseRegisterView, upgrade_me
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('about_user/', IndexView.as_view()),
    path('',
         LoginView.as_view(template_name='login/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='login/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='login/signup.html'),
         name='logout'),
    path('upgrade/', upgrade_me, name='upgrade')
]
