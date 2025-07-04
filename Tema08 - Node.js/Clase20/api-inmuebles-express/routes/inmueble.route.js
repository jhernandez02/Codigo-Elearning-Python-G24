const express = require('express');
const router = express.Router();
const inmuebleController = require('../controllers/inmueble.controller');

router.get('/', inmuebleController.listar);
router.get('/:id', inmuebleController.mostrarPorId);
router.post('/', inmuebleController.crear);
router.put('/:id', inmuebleController.actualizar);
router.delete('/:id', inmuebleController.eliminar);

module.exports = router;