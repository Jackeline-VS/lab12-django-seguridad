from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductoListView.as_view(), name='lista'),
    path('producto/nuevo/', views.crear_producto, name='crear_producto'),
    path('registro/', views.registro, name='registro'),
]