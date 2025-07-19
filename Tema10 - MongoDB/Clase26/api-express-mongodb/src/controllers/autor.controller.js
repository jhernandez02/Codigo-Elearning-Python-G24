const autorModel = require("../models/autor.model");

const controlador = {
    async listar(req, res){
        try {
            const result = await autorModel.find();
            res.json(result);
        } catch (error) {
            console.log('Error listar autor: ', error);
            res.sendStatus(500);
        }
    },
    async guardar(req, res){
        const { nombres, apellidos, nacionalidad } = req.body;
        try {
            const autor = new autorModel();
            autor.nombres = nombres;
            autor.apellidos = apellidos;
            autor.nacionalidad = nacionalidad;
            const result = await autor.save();
            res.json(result);
        } catch (error) {
            console.log('Error guardar autor: ', error);
            res.sendStatus(500);
        }
    },
    async buscarPorId(req, res){
        const { id } = req.params;
        try {
            const result = await autorModel.findById(id);
            res.json(result);
        } catch (error) {
            console.log('Error buscarPorId autor: ', error);
            res.sendStatus(500);
        }
    },
    async editar(req, res){
        const { id } = req.params;
        const { nombres, apellidos, nacionalidad, estado } = req.body;
        const updateData = { nombres, apellidos, nacionalidad, estado };
        const options = { 
            new:true, // devuelve el documento actualizado
            runValidators:true // verifica las validaciones como los valores de enum
        };
        try {
            const result = await autorModel.findByIdAndUpdate(id, updateData, options);
            res.json(result);
        } catch (error) {
            console.log('Error editar autor: ', error);
            res.sendStatus(500);
        }
    },
    async eliminar(req, res){
        const { id } = req.params;
        try {
            await autorModel.findByIdAndDelete(id);
            res.sendStatus(204);
        } catch (error) {
            console.log('Error eliminar autor: ', error);
            res.sendStatus(500);
        }
    },
};

module.exports = controlador;