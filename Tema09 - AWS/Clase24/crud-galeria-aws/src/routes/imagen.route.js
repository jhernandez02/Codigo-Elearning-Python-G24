import express from "express";
import imagenController from "../controllers/imagen.controller.js";

const router = express.Router();

router.get("/", imagenController.listar);
router.post("/", imagenController.crear);
router.get("/:id", imagenController.mostrarPorId);
router.put("/:id", imagenController.actualizar);
router.delete("/:id", imagenController.eliminar);

export default router;