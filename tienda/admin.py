from django.contrib import admin
from django.db.models import F
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'valor_inventario', 'creado')
    list_filter = ('creado',)
    search_fields = ('nombre',)
    readonly_fields = ('creado',)
    actions = ['reponer_stock']

    @admin.display(description='Valor inventario')
    def valor_inventario(self, obj):
        return obj.precio * obj.stock

    @admin.action(description='Reponer stock (+10)')
    def reponer_stock(self, request, queryset):
        cantidad = queryset.update(stock=F('stock') + 10)
        self.message_user(request, f'Stock repuesto en {cantidad} producto(s).')