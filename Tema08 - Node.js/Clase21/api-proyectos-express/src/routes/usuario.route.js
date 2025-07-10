import express from 'express';
const router = express.Router();
import usuarioController from '../controllers/usuario.controller.js';

router.get('/', usuarioController.listar);
router.get('/:id', usuarioController.mostrarPorId);
router.post('/', usuarioController.crear);
router.put('/:id', usuarioController.actualizar);
router.delete('/:id', usuarioController.eliminar);

export default router;