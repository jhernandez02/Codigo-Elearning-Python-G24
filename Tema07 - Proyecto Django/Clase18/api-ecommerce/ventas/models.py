from django.db import models
from almacen.models import Producto

# Create your models here.

class Pedido(models.Model):
    
    ESTADOS_LISTA = (
        ('Pendiente', 'PENDIENTE'),
        ('Completo',  'COMPLETADO'),
        ('Cancelado', 'CANCELADO')
    )

    # related_name define el nombre de la relación inversa que se podrá usar para acceder a los pedido de un usuario
    # Ej: usuario = User.objects.get(pk=36)
    #     pedidos_usuario = usuario.pedidos.all()
    cliente = models.ForeignKey('auth.User', on_delete=models.RESTRICT, related_name='pedidos')
    codigo = models.CharField(max_length=100)
    total = models.FloatField(default=0, editable=False)
    estado  = models.CharField(max_length=10, choices=ESTADOS_LISTA)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido {self.codigo}'

class PedidoDetalle(models.Model):
    # Ej: pedido = Pedido.objects.get(pk=458)
    #     detalle_pedido = pedido.detalles.all()
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    # Indicamos que este campo no sea editable desde el administrador web
    subtotal = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        # Calculamos el subtotal antes de guardar el objeto
        self.subtotal = self.cantidad * self.precio
        # Guardamos el detalle
        super().save(*args, **kwargs)