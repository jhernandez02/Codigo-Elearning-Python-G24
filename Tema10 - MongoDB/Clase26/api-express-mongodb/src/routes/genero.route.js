const express = require("express");
const router = express.Router();
const generoController = require("../controllers/genero.controller");

router.get('/', generoController.listar);
router.post('/', generoController.guardar);
router.get('/:id', generoController.buscarPorId);
router.put('/:id', generoController.editar);
router.delete('/:id', generoController.eliminar);

module.exports = router;