from django.urls import path
from . import views #importa as views do arquivo notas

app_name = 'user'

urlpatterns = [
    path('registro/', views.registro, name= "registro"),
    path('login/', views.login_user, name= "login"),
    path('logout/', views.logaut, name="logout"),
]
