from flask import Blueprint, request, jsonify
from models import db, Genero

genero_router = Blueprint('generos', __name__)

@genero_router.route('/generos', methods=['GET'])
def generos_index():
    generos = Genero.query.all()
    # Creamos el contenido mediante una lista por comprensión
    data = [{'id':genero.id, 'nombre':genero.nombre} for genero in generos]
    return jsonify(data)

@genero_router.route('/generos', methods=['POST'])
def generos_guardar():
    data = request.json
    nombre = data['nombre']
    genero = Genero(nombre=nombre)
    db.session.add(genero)
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Genero creado"
    })

@genero_router.route('/generos/<int:id>', methods=['GET'])
def genero_detalle(id):
    genero = Genero.query.get(id)
    return jsonify({
        "id": genero.id,
        "nombre": genero.nombre
    })

@genero_router.route('/generos/<int:id>', methods=['PUT'])
def generos_editar(id):
    data = request.json
    genero = Genero.query.get(id)
    genero.nombre = data['nombre']
    db.session.commit()
    return jsonify({
        "message": "Género actualizado"
    })

@genero_router.route('/generos/<int:id>', methods=['DELETE'])
def generos_eliminar(id):
    genero = Genero.query.get(id)
    db.session.delete(genero)
    db.session.commit()
    return jsonify({
        "message": "Género eliminado"
    })