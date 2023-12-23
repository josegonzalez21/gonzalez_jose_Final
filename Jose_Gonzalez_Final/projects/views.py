from pyexpat.errors import messages
from django import views
from django.http import JsonResponse
from django.urls import reverse_lazy
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import redirect, render
from .models import Inscrito, Institucion, Project
from .serializers import InscritoSerializer, InstitucionSerializer, ProjectForm, ProjectSerializer
from .forms import InscritoForm, InstitucionForm, Inscrito
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from rest_framework import generics





class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

class InscritoViewSet(viewsets.ModelViewSet):
    queryset = Inscrito.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InscritoSerializer

    def create(self, request, *args, **kwargs):
        if 'fecha_inscripcion' not in request.data:
            return Response({'error': 'fecha_inscripcion es un campo requerido'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InstitucionSerializer

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = InstitucionForm(request.POST)
            if form.is_valid():
                form.save()
                return Response({'message': 'Institución creada correctamente'}, status=status.HTTP_201_CREATED)
            else:
                return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Si la solicitud no es POST, renderiza el formulario
            form = InstitucionForm()
            return render(request, 'seminario/institucion_form.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def Listar(request):
    inscritos = Inscrito.objects.all()
    return render(request, 'listar_inscritos.html', {'inscritos': inscritos})

from django.shortcuts import render, redirect
from .forms import InscritoForm  # Asegúrate de importar tu formulario correctamente

from django.shortcuts import render, redirect
from .forms import InscritoForm  # Asegúrate de importar el formulario correcto

def agregar_inscrito(request):
    if request.method == 'POST':
        # Procesar el formulario si se envía
        form = InscritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Listar')  # Redirige a la página de listar inscritos
    else:
        # Si es una solicitud GET, simplemente renderiza el formulario vacío
        form = InscritoForm()

    return render(request, 'agregar_inscrito.html', {'form': form})

class ListarInstitucionesView(ListView):
    model = Institucion
    template_name = 'listar_instituciones.html'  # Reemplaza con el nombre correcto de tu template
    context_object_name = 'instituciones'

class AgregarInstitucionView(CreateView):
    model = Institucion
    form_class = InstitucionForm
    template_name = 'agregar_institucion.html'  # Reemplaza con el nombre correcto de tu template
    success_url = '/listar_instituciones/'

class ListarProyectosView(ListView):
    model = Project
    template_name = 'listar_proyectos.html'  # Asegúrate de ajustar la ruta correcta
    context_object_name = 'proyectos'

def AgregarProyectoView(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proyectos')
        else:
            print(form.errors)
    else:
        form = ProjectForm()

    return render(request, 'agregar_proyecto.html', {'form': form})
class InscritoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

class InscritoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer


class InscritoDeleteAPIView(generics.DestroyAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer



