let lista = require('../data/libro.data');
let nextId = 4;

const controlador = {
    listar(req, res){
        res.json(lista);
    },
    crear(req, res){
        const { titulo, autor } = req.body;
        const libro = {id: nextId, titulo, autor};
        nextId++;
        lista.push(libro);
        res.json(libro);
    },
    mostrarPorId(req, res){
        const { id } = req.params;
        const libro = lista.find(item=>item.id==id);
        res.json(libro);
    },
    actualizar(req, res){
        const { id } = req.params;
        const { titulo, autor } = req.body;
        const libro = lista.find(item=>item.id==id);
        libro.titulo = titulo;
        libro.autor = autor;
        res.json(libro);
    },
    eliminar(req, res){
        const { id } = req.params;
        lista = lista.filter(item=>item.id!=id);
        res.sendStatus(204);
    }
}

module.exports = controlador;