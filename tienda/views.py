from django.shortcuts import render, redirect
from .forms import ProductoForm


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_producto')
    else:
        form = ProductoForm()
    return render(request, 'tienda/form.html', {'form': form})