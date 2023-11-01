"""sisinf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from gameheaven import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.registerUser, name='registerUser'),
    path('login/', views.loginUser, name='loginUser'),
    path('home/', views.home, name = 'home'),
    path('', include('django.contrib.auth.urls')),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('settings/', views.settings, name='settings'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('delete_account/<int:id>/', views.deleteMyAccount, name='delete_account'),
    path('delete_trabajador/<int:id>/', views.deleteTrabajador, name='delete_trabajador'),
    path('reservas/', views.reservas, name='reservas'),
    path('gestionarTrabajadores/', views.gestionarTrabajadores, name='gestionarTrabajadores'),
    path('gestionarTiendas/', views.gestionarTiendas, name='gestionarTiendas'),
    path('add_trabajador/', views.addTrabajador, name='add_trabajador'),
    path('delete_shop/<int:idTienda>', views.delete_shop, name='delete_shop'),
    path('add_shop/', views.add_shop, name='add_shop'),
    path('producto/', views.producto, name='producto'),
    path('changeTienda/', views.changeTienda, name='changeTienda'),
]
