"""charity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url

from donation import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='main'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('form/', views.FormView.as_view(), name='form'),
    path('profile/', views.UserView.as_view(), name='profile'),
    path('edit_profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('change_password/', views.ChangePassword.as_view(), name='change-password'),
    path('donation_confirmed/', views.DonationConfirmation.as_view(), name='confirmation'),

]
