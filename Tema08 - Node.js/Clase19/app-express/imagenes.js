const express = require('express')
const app = express()
const port = 3000

// Definimos una carpeta estatica con un alias "uploads"
// Ejemplo: http://localhost:3000/uploads/img/planta.jpg
app.use('/uploads', express.static('public'))

// Middleware
app.use((req, res, next)=>{
    console.log(`Solicitado ${req.method} en ${req.url}`);
    next();
});

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})


