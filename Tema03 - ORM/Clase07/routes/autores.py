from flask import Blueprint, request, jsonify
from models import db, Autor

autor_router = Blueprint('autores', __name__)

@autor_router.route('/autores', methods=['GET'])
def autores_index():
    autores = Autor.query.all()
    # Creamos el contenido mediante una lista por comprensión
    data = [{'id':autor.id, 'nombre':autor.nombres, 'nacionalidad':autor.nacionalidad, 'fecha_nacimiento': autor.fecha_nacimiento} for autor in autores]
    return jsonify(data)

@autor_router.route('/autores', methods=['POST'])
def autores_guardar():
    data = request.json
    print('autores_guardar:', data)
    nombres = data['nombres']
    nacionalidad = data['nacionalidad']
    fecha_nacimiento = data['fecha_nacimiento']
    autor = Autor(nombres=nombres, nacionalidad=nacionalidad, fecha_nacimiento=fecha_nacimiento)
    db.session.add(autor)
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Autor creado"
    })

@autor_router.route('/autores/<int:id>', methods=['GET'])
def autores_detalle(id):
    autor = Autor.query.get(id)
    if autor:
        return jsonify({
            "id": autor.id,
            "nombres": autor.nombres,
            "nacionalidad": autor.nacionalidad,
            "fecha_nacimiento": autor.fecha_nacimiento
        })
    else:
        return jsonify({
            "message": "Autor no encontrado"
        })

@autor_router.route('/autores/<int:id>', methods=['PUT'])
def autores_editar(id):
    autor = Autor.query.get(id)
    if autor:
        data = request.json
        autor.nombres = data['nombres']
        autor.nacionalidad = data['nacionalidad']
        autor.fecha_nacimiento = data['fecha_nacimiento']
        db.session.commit()
        return jsonify({
            "message": "Autor actualizado"
        })
    else:
        return jsonify({
            "message": "Autor no encontrado"
        })

@autor_router.route('/autores/<int:id>', methods=['DELETE'])
def autores_eliminar(id):
    autor = Autor.query.get(id)
    if autor:
        db.session.delete(autor)
        db.session.commit()
        return jsonify({
            "message": "Autor eliminado"
        })
    else:
        return jsonify({
            "message": "Autor no encontrado"
        })
