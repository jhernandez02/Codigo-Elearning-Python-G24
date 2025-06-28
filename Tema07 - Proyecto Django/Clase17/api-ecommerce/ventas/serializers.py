from rest_framework import serializers
from .models import Pedido, PedidoDetalle

class PedidoDetalleSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    
    class Meta:
        model: PedidoDetalle
        fields = ['producto', 'producto_nombre', 'cantidad', 'precio', 'subtotal']

class PedidoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.get_full_name', read_only=True)
    detalles  = PedidoDetalleSerializer(many=True)

    class Meta:
        model: Pedido
        fields = ['id', 'cliente', 'cliente_nombre', 'codigo', 'total', 'estado', 'fecha_ventas', 'detalles']
        read_only_fields = ['total']