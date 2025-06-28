from django.contrib import admin
from .models import Pedido, PedidoDetalle

class PedidoDetalleInline(admin.TabularInline):
    model = PedidoDetalle
    extra = 0
    fields = ['producto','cantidad','precio', 'subtotal']
    readonly_fields = ['subtotal']

    class Media:
        js = ('admin/js/product_price_autofill.js',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('producto')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('codigo','cliente','total','estado','fecha_venta')
    readonly_fields = ['total']
    inlines = [PedidoDetalleInline]

    def save_formset(self, request, form, formset, change):
        pedido = form.instance
        total_precio = 0.0
        for inline_form in formset.cleaned_data:
            cantidad = inline_form.get('cantidad', 0)
            precio = inline_form.get('precio', 0)
            total_precio += cantidad * precio
        pedido.total = total_precio
        pedido.save() # Guardamos el pedido
        formset.save() # Guardamos el detalle

# Register your models here.
admin.site.register(Pedido, PedidoAdmin)