import express from 'express';
import loggerMiddleware from './middlewares/logger.middleware.js';
import validateMiddleware from './middlewares/validate.middleware.js';
import errorMiddleware from './middlewares/error.middleware.js';
import proyectoRutas from './routes/proyecto.route.js';
import usuarioRutas from './routes/usuario.route.js';

const app = express();
const port = 3000;

app.use(express.json());

// Middleware de aplicación
app.use(loggerMiddleware);

app.get('/', (req, res)=>{
  res.send('Hola Express.js');
});

app.use('/api/proyectos', proyectoRutas);
// Middleware específico para rutas
app.use('/api/usuarios', validateMiddleware, usuarioRutas);

app.get('/error', (req, res)=>{
  throw new Error('¡Ha ocurrido un error!');
});

//Middleware de manejo de error
app.use(errorMiddleware);

app.listen(port, ()=>{
  console.log(`Servidor ejecutandose en el puerto ${port}`);
});