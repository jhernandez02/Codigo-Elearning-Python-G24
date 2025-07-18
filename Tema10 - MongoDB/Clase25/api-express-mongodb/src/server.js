const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const PORT = 3000;

require("dotenv").config();

mongoose.connect(process.env.DATABASE_URL)
.then(()=>console.log("Conectados a la base de datos!"))
.catch((error)=>console.log("Error al conectar a la bvase de datos: ", error));

const app = express();

app.use(cors());
app.use(express.json());

app.listen(PORT, ()=>console.log(`Servidor iniciado en el puerto ${PORT}`));
