from django import forms
from rest_framework import serializers
from .models import Institucion, Inscrito , Project

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'
        read_only_fields = ('id','fecha_creacion')

class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrito
        fields = '__all__'
        read_only_fields = ('id_instcrito', 'hora_inscripcion')
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrito
        fields = '__all__'

