
from django.urls import path
from docente import views

urlpatterns = [
    path("",views.index, name="docente"),
    path("view/<int:id>", views.view, name="docente_view"),
    path("edit/<int:id>", views.edit, name="docente_edit"),
    path("create/",views.create, name="docente_create"),
    path("delete/<int:id>/",views.delete, name="docente_delete"),
]