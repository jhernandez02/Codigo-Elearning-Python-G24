import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

const controlador = {
    async listar(req, res){
        const data = await prisma.imagen.findMany();
        res.json(data);
    },
    async crear(req, res){
        const { descripcion, archivo, url } = req.body;
        const imagen = await prisma.imagen.create({
            data: { descripcion, archivo, url }
        });
        res.json(imagen);
    },
    async mostrarPorId(req, res){
        const { id } = req.params;
        const imagen = await prisma.imagen.findUnique({
            where: { id: parseInt(id) }
        });
        res.json(imagen);
    },
    async actualizar(req, res){
        const { id } = req.params;
        const { descripcion } = req.body;
        const actualizado = await prisma.imagen.update({
            where: { id: parseInt(id) },
            data: { descripcion }
        });
        res.json(actualizado);
    },
    async eliminar(req, res){
        const { id } = req.params;
        await prisma.imagen.delete({
            where: { id: parseInt(id) },
        });
        res.sendStatus(204);
    }
};

export default controlador;