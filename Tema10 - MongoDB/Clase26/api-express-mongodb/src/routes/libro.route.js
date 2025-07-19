const express = require("express");
const router = express.Router();
const libroController = require("../controllers/libro.controller");

router.get('/', libroController.listar);
router.post('/', libroController.guardar);
router.get('/:id', libroController.buscarPorId);
router.put('/:id', libroController.editar);
router.delete('/:id', libroController.eliminar);

module.exports = router;