import listaProyecto from '../data/proyecto.data.js';
let lista = [...listaProyecto];
let nextId = 4;

const controlador = {
    listar(req, res){
        res.json(lista);
    },
    crear(req, res){
        const { nombre } = req.body;
        const proyecto  = {
            id: nextId,
            nombre
        };
        lista.push(proyecto);
        nextId++;
        res.json(proyecto);
    },
    mostrarPorId(req, res){
        const { id } = req.params;
        const proyecto = lista.find(item=>item.id==id);
        res.json(proyecto);
    },
    actualizar(req, res){
        const { id } = req.params;
        const { nombre } = req.body;
        const proyecto = lista.find(item=>item.id==id);
        proyecto.nombre = nombre;
        res.json(proyecto);
    },
    eliminar(req, res){
        const { id } = req.params;
        lista = lista.filter(item=>item.id!=id);
        res.sendStatus(204);
    }
};

export default controlador;