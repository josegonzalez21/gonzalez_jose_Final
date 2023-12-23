from django.contrib import admin
from django.urls import path, include
from projects import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include('projects.urls')),
    path('', views.index, name='index'),
    path('Listar', views.Listar, name='Listar'),
    path('agregar_inscrito/', views.agregar_inscrito, name='agregar_inscrito'),
    path('listar_instituciones/', views.ListarInstitucionesView.as_view(), name='listar_instituciones'),
    path('agregar_institucion/', views.AgregarInstitucionView.as_view(), name='agregar_institucion'),
    path('listar_proyectos/', views.ListarProyectosView.as_view(), name='listar_proyectos'),
    path('agregar_proyecto/', views.AgregarProyectoView, name='agregar_proyecto'),
    path('inscritos/<int:pk>/delete/', views.InscritoDeleteAPIView.as_view(), name='inscrito-delete'),

]
