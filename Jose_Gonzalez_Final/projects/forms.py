from django import forms
from .models import Institucion, Inscrito

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre', 'direccion', 'telefono', 'correo', 'sitio_web']

class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = '__all__'  # Esto incluirá todos los campos de tu modelo en el formulario

    def __init__(self, *args, **kwargs):
        super(InscritoForm, self).__init__(*args, **kwargs)
        # Puedes personalizar la apariencia del formulario aquí si lo necesitas
        # Por ejemplo, puedes agregar clases de Bootstrap a los campos
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
