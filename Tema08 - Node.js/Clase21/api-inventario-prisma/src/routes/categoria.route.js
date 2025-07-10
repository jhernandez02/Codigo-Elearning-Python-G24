import express from 'express';
import categoriaController from '../controllers/categoria.controller.js';

const router = express.Router();

router.get('/', categoriaController.listar);
router.post('/', categoriaController.crear);
router.get('/:id', categoriaController.mostrarPorId);
router.put('/:id', categoriaController.actualizar);
router.delete('/:id', categoriaController.eliminar);

export default router;