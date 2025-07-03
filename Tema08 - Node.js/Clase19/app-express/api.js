const express = require('express')
const app = express()
const port = 3200

app.use(express.json());

let lista = [
    {id:1, marca:"Toyota", "modelo": "Rav6"},
    {id:2, marca:"Kia", "modelo": "Sportage"},
    {id:3, marca:"Hyundai", "modelo": "Tucsan"},
];
let nextId = 4;

app.get('/', (req, res) => {
    res.json(lista)
})

app.post('/', (req, res) => {
    const { marca, modelo } = req.body;
    const auto = {id:nextId, marca: marca, modelo: modelo};
    lista.push(auto);
    nextId++;
    res.json(auto)
})

app.get('/:id', (req, res) => {
    const { id } = req.params;
    const auto = lista.find(item => item.id == id);
    res.json(auto)
})

app.put('/:id', (req, res) => {
    const { id } = req.params;
    const { marca, modelo } = req.body;
    const auto = lista.find(item => item.id == id);
    auto.marca = marca;
    auto.modelo = modelo;
    res.json(auto)
})

app.delete('/:id', (req, res) => {
    const { id } = req.params;
    lista = lista.filter(item => item.id!=id);
    res.sendStatus(204);
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})
