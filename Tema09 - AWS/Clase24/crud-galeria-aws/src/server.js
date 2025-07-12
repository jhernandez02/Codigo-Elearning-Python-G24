import express from "express";
import imagenRutas from "./routes/imagen.route.js";

const app = express();
const port = 3000;

app.use(express.json());

app.get("/", (req, res)=>res.send("Hola AWS"));

app.use("/api/imagenes", imagenRutas);

app.listen(port, ()=>console.log(`Servidor iniciado en el puerto ${port}`));