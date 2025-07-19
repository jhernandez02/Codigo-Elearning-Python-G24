const mongoose = require("mongoose");
const Schema  = mongoose.Schema;

const collectionSchema = new Schema({
    nombres: { type:String, required: true },
    apellidos: { type:String, required: true },
    nacionalidad: { type:String, required: true },
    fecha_nacimiento: Date,
    biografia: String,
    fecha_creacion: { type:Date, default:Date.now },
    estado: { type:String, enum:['A','I'], default:'A' } // A:activo | I:inactivo
},{
    versionKey: false
});
// La colección que se crea en MongoDB será "autores"
// definido en el último parámetro.
module.exports = mongoose.model('autor', collectionSchema, "autores");