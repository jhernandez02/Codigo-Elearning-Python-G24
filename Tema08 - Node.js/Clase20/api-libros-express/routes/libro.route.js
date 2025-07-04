const express = require('express');
const router = express.Router();
const libroController = require('../controllers/libro.controller');

router.get('/', libroController.listar);
router.get('/:id', libroController.mostrarPorId);
router.post('/', libroController.crear);
router.put('/:id', libroController.actualizar);
router.delete('/:id', libroController.eliminar);

module.exports = router;