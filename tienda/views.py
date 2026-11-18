from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import ProductoForm
from .models import Producto


@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = ProductoForm()
    return render(request, 'tienda/form.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tienda/registro.html', {'form': form})


class ProductoListView(PermissionRequiredMixin, ListView):
    model = Producto
    permission_required = 'tienda.view_producto'
    template_name = 'tienda/lista.html'
    context_object_name = 'productos'