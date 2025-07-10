import express from 'express';
import productoController from '../controllers/producto.controller.js';

const router = express.Router();

router.get('/', productoController.listar);
router.get('/:id', productoController.mostrarPorId);
router.post('/', productoController.crear);
router.put('/:id', productoController.actualizar);
router.delete('/:id', productoController.eliminar);

export default router;