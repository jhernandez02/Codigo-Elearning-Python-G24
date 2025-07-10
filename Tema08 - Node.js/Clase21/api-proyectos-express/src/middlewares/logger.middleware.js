const loggerMiddleware = (req, res, next) => {
  console.log(`Solicitando ${req.method} en ${req.url}`);
  next();
}

export default loggerMiddleware;