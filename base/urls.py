from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('',views.login, name='login'),
    path('login',views.login, name='login'),
    path('logout',views.login, name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('vehicles/',views.vehicles, name='vehicles'),
    path('create-vehicle/',views.createVehicle, name='create-vehicle'),
    path('update-vehicle/<str:id>',views.updateVehicle, name='update-vehicle'),
    path('delete-vehicle/<str:id>',views.deleteVehicle, name='delete-vehicle'),
    path('users/',views.users, name='users'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html')),
    #path('password/',views.userPassword, name='password'),
    path('update-user/<str:id>',views.updateUser, name='update-user'),
]