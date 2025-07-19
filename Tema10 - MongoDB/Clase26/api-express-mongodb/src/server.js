const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const PORT = 3000;

const generoRutas = require("./routes/genero.route");
const autorRutas = require("./routes/autor.route");
const libroRutas = require("./routes/libro.route");

require("dotenv").config();

mongoose.connect(process.env.DATABASE_URL)
.then(()=>console.log("Conectados a la base de datos!"))
.catch((error)=>console.log("Error al conectar a la base de datos: ", error));

const app = express();

app.use(cors());
app.use(express.json());

app.use('/api/generos', generoRutas);
app.use('/api/autores', autorRutas);
app.use('/api/libros', libroRutas);

app.listen(PORT, ()=>console.log(`Servidor iniciado en el puerto ${PORT}`));
