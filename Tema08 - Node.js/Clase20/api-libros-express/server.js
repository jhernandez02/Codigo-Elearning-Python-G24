const express = require('express');
const app = express();
const port = 3000;

const libroRutas = require('./routes/libro.route');

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hola Express')
});

app.use('/api/libros', libroRutas);

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
});
