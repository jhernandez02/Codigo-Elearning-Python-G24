let lista = require('../data/inmueble.data');
let nextId = 4;

const controlador = {
    listar(req, res){
        return res.json(lista);
    },
    crear(req, res){
        console.log('req.body:', req.body);
        const inmueble = {id:nextId, ...req.body};
        nextId++;
        console.log(inmueble);
        lista.push(inmueble);
        res.json(inmueble);
    },
    mostrarPorId(req, res){
        const { id } = req.params;
        const inmueble = lista.find(item=>item.id==id);
        res.json(inmueble);
    },
    actualizar(req, res){
        const { id } = req.params;
        const { tipo, titulo, descripcion, direccion, precio } = req.body;
        const inmueble = lista.find(item=>item.id==id);
        inmueble.tipo = tipo;
        inmueble.titulo = titulo;
        inmueble.descripcion = descripcion;
        inmueble.direccion = direccion;
        inmueble.precio = precio;
        res.json(inmueble);
    },
    eliminar(req, res){
        const { id } = req.params;
        lista = lista.filter(item=>item.id!=id);
        res.sendStatus(204);
    }
};

module.exports = controlador;