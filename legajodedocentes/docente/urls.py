
from django.urls import path
from docente import views

urlpatterns = [
    # todo esto son rutas de docentes
    path("",views.index, name="docente"),
    path("view/<int:id>", views.view, name="docente_view"),
    path("edit/<int:id>", views.edit, name="docente_edit"),
    path("create/",views.create, name="docente_create"),
    path("delete/<int:id>/",views.delete, name="docente_delete"),

    # aca esto son las rutas de los documentos
    path("documento/",views.documento, name="documento"),
    path("create_document/", views.create_document, name="create_document"),
    path("edit_document/<int:id>", views.edit_document, name="edit_document")

]