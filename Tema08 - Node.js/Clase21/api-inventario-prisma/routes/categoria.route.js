import express from 'express';
import { PrismaClient } from '@prisma/client';

const router = express.Router();
const prisma = new PrismaClient();

router.get('/', async (req, res)=>{
    const data = await prisma.categoria.findMany();
    res.json(data);
});

router.post('/', async (req, res)=>{
    const { nombre } = req.body;
    const categoria = await prisma.categoria.create({
        data: { nombre }
    });
    res.json(categoria);
});

export default router;