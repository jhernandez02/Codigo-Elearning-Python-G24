from flask import Blueprint, request, jsonify
from models import db, Libro

libro_router = Blueprint('libros', __name__)

@libro_router.route('/libros', methods=['GET'])
def libros_index():
    libros = Libro.query.all()
    # Creamos el contenido mediante una lista por comprensión
    data = [{'id':libro.id, 'titulo':libro.titulo, 'autor':libro.autor.nombres, 'genero': libro.genero.nombre, 'isbn':libro.isbn, 'estado':libro.estado} for libro in libros]
    return jsonify(data)

@libro_router.route('/libros', methods=['POST'])
def libros_guardar():
    data = request.json
    titulo = data['titulo']
    autor = data['autor_id']
    genero = data['genero_id']
    isbn = data['isbn']
    libro = Libro(titulo=titulo, autor_id=autor, genero_id=genero, isbn=isbn)
    db.session.add(libro)
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Libro creado"
    })

@libro_router.route('/libros/<int:id>', methods=['GET'])
def libros_detalle(id):
    libro = Libro.query.get(id)
    if libro:
        return jsonify({
            "id": libro.id,
            "titulo": libro.titulo,
            "genero": libro.genero.nombre,
            "autor": libro.autor.nombres,
            "isbn": libro.isbn,
            "estado": libro.estado,
        })
    else:
        return jsonify({
            "message": "Libro no encontrado"
        })

@libro_router.route('/libros/<int:id>', methods=['PUT'])
def libros_editar(id):
    libro = Libro.query.get(id)
    if libro:
        data = request.json
        libro.titulo = data['titulo']
        libro.autor_id = data['autor_id']
        libro.genero_id = data['genero_id']
        libro.isbn = data['isbn']
        libro.estado = data['estado']
        db.session.commit()
        return jsonify({
            "message": "Libro actualizado"
        })
    else:
        return jsonify({
            "message": "Libro no encontrado"
        })

@libro_router.route('/libros/<int:id>', methods=['DELETE'])
def libros_eliminar(id):
    libro = Libro.query.get(id)
    if libro:
        db.session.delete(libro)
        db.session.commit()
        return jsonify({
            "message": "Libro eliminado"
        })
    else:
        return jsonify({
            "message": "Libro no encontrado"
        })