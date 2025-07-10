const validateMiddleware = (req, res, next) => {
    // No se puede crear un usuario tipo admin
    if(req.method=='POST' && req.body.rol=='admin'){
        res.json({message: "no permitido"})
    }
    next();
}

export default validateMiddleware;