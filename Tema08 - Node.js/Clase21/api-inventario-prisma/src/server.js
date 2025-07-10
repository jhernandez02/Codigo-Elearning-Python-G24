import express from 'express';
import categoriaRutas from './routes/categoria.route.js';
import productoRutas from './routes/producto.route.js';

const app = express();
const port = 3000;

app.use(express.json());

app.get('/', (req, res)=>{
  res.send('Hola Express.js');
});

app.use('/api/categorias', categoriaRutas);
app.use('/api/productos', productoRutas);

app.listen(port, ()=>{
  console.log(`Servidor ejecutandose en el puerto ${port}`);
});