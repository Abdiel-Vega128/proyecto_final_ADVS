from django.urls import path
from .views import (
    DuenoListView, DuenoDetailView, DuenoCreateView, DuenoUpdateView, DuenoDeleteView,
    VeterinarioListView, VeterinarioDetailView, VeterinarioCreateView, VeterinarioUpdateView, VeterinarioDeleteView,
    MascotaListView, MascotaDetailView, MascotaCreateView, MascotaUpdateView, MascotaDeleteView,
    ConsultaListView, ConsultaDetailView, ConsultaCreateView, ConsultaUpdateView, ConsultaDeleteView,
    VacunaListView, VacunaDetailView, VacunaCreateView, VacunaUpdateView, VacunaDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('duenos/', DuenoListView.as_view(), name='dueno_list'),
    path('duenos/<int:pk>/', DuenoDetailView.as_view(), name='dueno_detail'),
    path('duenos/nuevo/', DuenoCreateView.as_view(), name='dueno_create'),
    path('duenos/<int:pk>/editar/', DuenoUpdateView.as_view(), name='dueno_update'),
    path('duenos/<int:pk>/eliminar/', DuenoDeleteView.as_view(), name='dueno_delete'),

    path('veterinarios/', VeterinarioListView.as_view(), name='veterinario_list'),
    path('veterinarios/<int:pk>/', VeterinarioDetailView.as_view(), name='veterinario_detail'),
    path('veterinarios/nuevo/', VeterinarioCreateView.as_view(), name='veterinario_create'),
    path('veterinarios/<int:pk>/editar/', VeterinarioUpdateView.as_view(), name='veterinario_update'),
    path('veterinarios/<int:pk>/eliminar/', VeterinarioDeleteView.as_view(), name='veterinario_delete'),

    path('mascotas/', MascotaListView.as_view(), name='mascota_list'),
    path('mascotas/<int:pk>/', MascotaDetailView.as_view(), name='mascota_detail'),
    path('mascotas/nuevo/', MascotaCreateView.as_view(), name='mascota_create'),
    path('mascotas/<int:pk>/editar/', MascotaUpdateView.as_view(), name='mascota_update'),
    path('mascotas/<int:pk>/eliminar/', MascotaDeleteView.as_view(), name='mascota_delete'),

    path('consultas/', ConsultaListView.as_view(), name='consulta_list'),
    path('consultas/<int:pk>/', ConsultaDetailView.as_view(), name='consulta_detail'),
    path('consultas/nuevo/', ConsultaCreateView.as_view(), name='consulta_create'),
    path('consultas/<int:pk>/editar/', ConsultaUpdateView.as_view(), name='consulta_update'),
    path('consultas/<int:pk>/eliminar/', ConsultaDeleteView.as_view(), name='consulta_delete'),

    path('vacunas/', VacunaListView.as_view(), name='vacuna_list'),
    path('vacunas/<int:pk>/', VacunaDetailView.as_view(), name='vacuna_detail'),
    path('vacunas/nuevo/', VacunaCreateView.as_view(), name='vacuna_create'),
    path('vacunas/<int:pk>/editar/', VacunaUpdateView.as_view(), name='vacuna_update'),
    path('vacunas/<int:pk>/eliminar/', VacunaDeleteView.as_view(), name='vacuna_delete'),
]
