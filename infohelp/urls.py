from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.inicio, name="inicio"),
    path('cursos/', views.cursos, name="cursos"),
    path('biblioteca/', views.biblioteca, name="biblioteca"),
    path('login/', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),
]