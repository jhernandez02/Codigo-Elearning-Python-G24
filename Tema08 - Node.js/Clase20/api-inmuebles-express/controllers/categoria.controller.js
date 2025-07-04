let lista = require('../data/categoria.data');
let nextId = 4;

const controlador = {
    listar(req, res){
        return res.json(lista);
    },
    crear(req, res){
        const { nombre } = req.body;
        const categoria = {id: nextId, nombre};
        nextId++;
        lista.push(categoria);
        res.json(categoria);
    },
    mostrarPorId(req, res){
        const { id } = req.params;
        const categoria = lista.find(item=>item.id==id);
        res.json(categoria);
    },
    actualizar(req, res){
        const { id } = req.params;
        const { nombre } = req.body;
        const categoria = lista.find(item=>item.id==id);
        categoria.nombre = nombre;
        res.json(categoria);
    },
    eliminar(req, res){
        const { id } = req.params;
        lista = lista.filter(item=>item.id!=id);
        res.sendStatus(204);
    }
};

module.exports = controlador;