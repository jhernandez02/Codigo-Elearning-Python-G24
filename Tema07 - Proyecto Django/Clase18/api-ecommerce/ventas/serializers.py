from rest_framework import serializers
from .models import Pedido, PedidoDetalle

class PedidoDetalleSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    
    class Meta:
        model = PedidoDetalle
        fields = ['producto', 'producto_nombre', 'cantidad', 'precio', 'subtotal']

class PedidoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.get_full_name', read_only=True)
    detalles  = PedidoDetalleSerializer(many=True)
    
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'cliente_nombre', 'codigo', 'total', 'estado', 'fecha_venta', 'detalles']
        read_only_fields = ['cliente', 'total', 'estado'] # Estos campos no deben enviarse

    def create(self, validated_data):
        print(validated_data)
        
        # Extraemos los detalle del pedido
        detalle_pedido = validated_data.pop('detalles')
        
        # Creamos el pedido
        pedido = Pedido.objects.create(**validated_data, estado='Pendiente')
        
        # Definimos el acumulador total
        total = 0

        # Creamos los detalles del pedido
        for detalle in detalle_pedido:
            PedidoDetalle.objects.create(pedido=pedido, **detalle)
            # Calculamos el total acumulado
            total += detalle['cantidad'] * detalle['precio']

        # Actualizamos el pedido
        pedido.total = round(total, 2)
        pedido.save()

        return pedido

class BoletaItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    cantidad = serializers.IntegerField(required=True, min_value=0)

class BoletaSerializer(serializers.Serializer):
    documento_usuario = serializers.CharField(min_length=8, max_length=8, allow_null=False, required=True)
    nombre_usuario = serializers.CharField(required=True)
    items = BoletaItemSerializer(many=True)
