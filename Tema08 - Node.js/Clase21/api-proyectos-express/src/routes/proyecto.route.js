import express from 'express';
const router = express.Router();
import proyectoController from '../controllers/proyecto.controller.js';

router.get('/', proyectoController.listar);
router.get('/:id', proyectoController.mostrarPorId);
router.post('/', proyectoController.crear);
router.put('/:id', proyectoController.actualizar);
router.delete('/:id', proyectoController.eliminar);

export default router;