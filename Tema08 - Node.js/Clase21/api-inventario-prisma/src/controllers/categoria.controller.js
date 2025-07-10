import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

const controlador = {
    async listar(req, res){
        const data = await prisma.categoria.findMany({
            orderBy: {
                nombre: 'asc'
            }
        });
        res.json(data);
    },
    async crear(req, res){
        const { nombre } = req.body;
        const categoria = await prisma.categoria.create({
            data: { nombre }
        });
        res.json(categoria);
    },
    async mostrarPorId(req, res){
        const { id } = req.params;
        const categoria = await prisma.categoria.findUnique({
            where: { id: parseInt(id) }
        });
        res.json(categoria);
    },
    async actualizar(req, res){
        const { id } = req.params;
        const { nombre } = req.body;
        const actualizada = await prisma.categoria.update({
            where: { id: parseInt(id) },
            data: { nombre }
        });
        res.json(actualizada);
    },
    async eliminar(req, res){
        const { id } = req.params;
        await prisma.categoria.delete({
             where: { id: parseInt(id) }
        });
        res.sendStatus(204);
    }
};

export default controlador;