from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from almacen.models import Producto
from .models import Pedido
from .serializers import PedidoSerializer, BoletaSerializer
from datetime import datetime
import os
import requests

# Create your views here.

@api_view(['GET'])
def listar_pedido(request):
    user = request.user
    pedidos = Pedido.objects.filter(cliente=user)
    serializer = PedidoSerializer(pedidos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_pedido(request):
    serializer = PedidoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(cliente=request.user)
        return Response({"message": "ok"})
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def generar_boleta(request):
    serializer = BoletaSerializer(data=request.data)
    if serializer.is_valid():
        item = {
            'unidad_de_medida': 'NIU',
            'codigo': 'PROD00001',
            'descripcion': 'Licuadora Akita',
            'cantidad': 1,
            'valor_unitario': 100.00,
            'precio_unitario': 118.00,
            'subtotal': 100.00,
            'tipo_de_igv': 1,
            'igv': 18.00,
            'total': 118.00,
            'anticipo_regularizacion': False
        }
        data = {
            'operacion': 'generar_comprobante',
            'tipo_de_comprobante': 2,
            'serie': 'BBB1',
            'numero': 1,
            'sunat_transaction': 1,
            'cliente_tipo_de_documento': 1,
            'cliente_numero_de_documento': '87654321',
            'cliente_denominacion': 'Jhon García',
            'fecha_de_emision': datetime.now().strftime('%d-%m-%Y'),
            'moneda': 1,
            'total_igv': 18.00,
            'total_gravada': 100.00,
            'porcentaje_de_igv': 18.00,
            'total': 118.00,
            'items': [item]
        }
        
        nubefact_url= os.getenv('NUBEFACT_URL')
        nubefact_token = os.getenv('NUBEFACT_TOKEN')
        headers = {'Authorization': 'Bearer '+nubefact_token}

        response = requests.post(url=nubefact_url, headers=headers, json=data)
        print(response.status_code)
        print(response.json())

        return Response({"message": "Boleta creada existosamente","data": data})
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def get_producto_precio(request, producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
        return JsonResponse({'precio': str(producto.precio)})
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)
