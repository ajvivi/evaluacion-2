from django.urls import path
from . import views

app_name = "inicio"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("naturaleza/", views.tema1, name="tema1"),
    path("tecnologia/", views.tema2, name="tema2"),
]