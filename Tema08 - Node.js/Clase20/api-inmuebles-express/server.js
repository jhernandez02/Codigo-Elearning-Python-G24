const express = require('express');
const inmuebleRutas = require('./routes/inmueble.route');
const categoriaRutas = require('./routes/categoria.route');
const app = express();
const port = 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hola Express')
});

app.use('/api/inmuebles', inmuebleRutas);
app.use('/api/categorias', categoriaRutas);

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
