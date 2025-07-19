const express = require("express");
const router = express.Router();
const autorController = require("../controllers/autor.controller");

router.get('/', autorController.listar);
router.post('/', autorController.guardar);
router.get('/:id', autorController.buscarPorId);
router.put('/:id', autorController.editar);
router.delete('/:id', autorController.eliminar);

module.exports = router;