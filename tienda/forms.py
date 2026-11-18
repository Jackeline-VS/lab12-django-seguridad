import re
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import Producto

validar_nombre = RegexValidator(
    regex=r'^[A-Za-z0-9ÁÉÍÓÚáéíóúÑñ ._-]+$',
    message='El nombre solo admite letras, números, espacios, punto, guion y guion bajo.'
)


def sanitize_input(texto):
    """Quita etiquetas HTML, recorta y colapsa espacios."""
    texto = re.sub(r'<[^>]*>', '', texto)
    return re.sub(r'\s+', ' ', texto).strip()


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs['class'] = 'form-control'
        self.fields['nombre'].validators.append(validar_nombre)

    def clean_nombre(self):
        nombre = sanitize_input(self.cleaned_data['nombre'])
        if len(nombre) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre.title()

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise ValidationError('El precio debe ser mayor que 0.')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock > 10000:
            raise ValidationError('El stock no puede superar 10 000 unidades.')
        return stock

    def clean(self):
        datos = super().clean()
        nombre = datos.get('nombre')
        precio = datos.get('precio')
        stock = datos.get('stock')
        if nombre and nombre.lower() == 'admin':
            self.add_error('nombre', 'Ese nombre está reservado.')
        if precio and stock is not None and precio >= 1000 and stock > 100:
            raise ValidationError(
                'Un producto de precio alto (>= 1000) no puede tener más de 100 unidades.'
            )
        return datos


class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=80)
    correo = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs['class'] = 'form-control'