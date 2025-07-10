import express from 'express';
import categoriaRutas from './routes/categoria.route.js';
const app = express();
const port = 3000;

app.use(express.json());

app.get('/', (req, res)=>{
  res.send('Hola Express.js');
});

app.use('/api/categorias', categoriaRutas);

app.listen(port, ()=>{
  console.log(`Servidor ejecutandose en el puerto ${port}`);
});