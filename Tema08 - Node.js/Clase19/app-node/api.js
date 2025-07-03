const http = require('http');

let lista = [
    {id:1, marca:"Toyota", "modelo": "Rav6"},
    {id:2, marca:"Kia", "modelo": "Sportage"},
    {id:3, marca:"Hyundai", "modelo": "Tucsan"},
];
let nextId = 4;

const server = http.createServer((req, res) => {
    console.log('método: ', req.method);
    console.log('url: ', req.url)
    res.setHeader('Content-Type', 'application/json');
    if(req.method=='GET'){
        res.end(JSON.stringify(lista));
    }else if(req.method=='POST'){
        let body = "";
        req.on('data', chunk => body += chunk);
        req.on('end', ()=>{
            const data = JSON.parse(body);
            const auto = {id:nextId, marca: data.marca, modelo: data.modelo};
            lista.push(auto);
            nextId++;
            res.writeHead(201);
            res.end(JSON.stringify(auto));
        });
    }else if(req.method=='PUT'){
        const id = req.url.split('/')[1];
        console.log('id:', id);
        let body = "";
        req.on('data', chunk => body += chunk);
        req.on('end', ()=>{
            const data = JSON.parse(body);
            const auto = lista.find(item => item.id == id);
            auto.marca = data.marca;
            auto.modelo = data.modelo;
            res.end(JSON.stringify(auto));
        });
    }else if(req.method=='DELETE'){
        const id = req.url.split('/')[1];
        lista = lista.filter(item => item.id!=id);
        res.writeHead(204);
        res.end();
    }else {
        const message = {error: 'Método no soportado'};
        res.writeHead(405);
        res.end(JSON.stringify(message));
    }
});

// starts a simple http server locally on port 3000
server.listen(3000, () => {
  console.log('Listening on 3000');
});