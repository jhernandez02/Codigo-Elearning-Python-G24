import listaUsuario from '../data/usuario.data.js';
let lista = [...listaUsuario];
let nextId = 4;

const controlador = {
    listar(req, res){
        res.json(lista);
    },
    crear(req, res){
        const { nombres, rol, email } = req.body;
        const usuario  = {
            id: nextId,
            nombres,
            rol,
            email
        };
        lista.push(usuario);
        nextId++;
        res.json(usuario);
    },
    mostrarPorId(req, res){
        const { id } = req.params;
        const usuario = lista.find(item=>item.id==id);
        res.json(usuario);
    },
    actualizar(req, res){
        const { id } = req.params;
        const { nombres, rol, email } = req.body;
        const usuario = lista.find(item=>item.id==id);
        usuario.nombres = nombres;
        usuario.rol = rol;
        usuario.email = email;
        res.json(usuario);
    },
    eliminar(req, res){
        const { id } = req.params;
        lista = lista.filter(item=>item.id!=id);
        res.sendStatus(204);
    }
};

export default controlador;