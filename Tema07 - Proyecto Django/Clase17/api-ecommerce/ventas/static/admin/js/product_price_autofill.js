window.onload = function(){
    const $ = django.jQuery;
    $('.inline-related select').change(function(){
        const producto_id = this.value;
        const productoSelectId = this.id; // Ej: id_detalles-2-producto
        console.log('Consultamos el precio del producto:', productoSelectId);
        const precioInputId = productoSelectId.replace('-producto','-precio');
        console.log('Asigamos el precio del producto:', precioInputId);
        if(producto_id!=''){
            // Consultamos el precio del producto mediante el endpoint
            $.get(`/api/v1/ventas/producto/${producto_id}`, function(data){
                // La respuesta del servidor se guarda en la variable "data"
                console.log('data:', data);
                $('#'+precioInputId).val(data.precio);
            });
        }else{
            $('#'+precioInputId).val('');
        }
    });
};