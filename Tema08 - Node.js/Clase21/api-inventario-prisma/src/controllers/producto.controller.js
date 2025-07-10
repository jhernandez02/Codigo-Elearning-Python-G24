import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

const controlador = {
    async listar(req, res){
        const data = await prisma.producto.findMany({
            select : {
                id: true,
                nombre: true,
                categoria: {
                    select: { nombre: true }
                }
            },
            orderBy: {
                nombre: 'asc'
            }
        });
        res.json(data);
    },
    async crear(req, res){
        const { categoriaId, codigo, nombre, precio, cantidad, fecha_compra } = req.body;
        const producto = await prisma.producto.create({
            data: { categoriaId, codigo, nombre, precio, cantidad, fecha_compra }
        });
        res.json(producto);
    },
    async mostrarPorId(req, res){
        const { id } = req.params;
        const producto = await prisma.producto.findUnique({
            where: { id: parseInt(id) },
            include: {
                categoria: {
                    select: { nombre: true }
                }
            }
        });
        res.json(producto);
    },
    async actualizar(req, res){
        const { id } = req.params;
        const { categoriaId, codigo, nombre, precio, cantidad, fecha_compra } = req.body;
        const actualizada = await prisma.producto.update({
            where: { id: parseInt(id) },
            data: { categoriaId, codigo, nombre, precio, cantidad, fecha_compra  }
        });
        res.json(actualizada);
    },
    async eliminar(req, res){
        const { id } = req.params;
        await prisma.producto.delete({
             where: { id: parseInt(id) }
        });
        res.sendStatus(204);
    }
}

export default controlador;