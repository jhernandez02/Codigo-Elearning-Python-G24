from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Genero, Autor
from dotenv import load_dotenv
import os

# Cargamos las variables desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

# Inicializamos la aplicación
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello_world():
    return "<p>Hola, Mundo!</p>"

@app.route('/generos', methods=['GET'])
def generos_index():
    generos = Genero.query.all()
    # Creamos el contenido mediante una lista por comprensión
    data = [{'id':genero.id, 'nombre':genero.nombre} for genero in generos]
    return jsonify(data)

@app.route('/generos', methods=['POST'])
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

@app.route('/generos/<int:id>', methods=['GET'])
def genero_detalle(id):
    genero = Genero.query.get(id)
    return jsonify({
        "id": genero.id,
        "nombre": genero.nombre
    })

@app.route('/generos/<int:id>', methods=['PUT'])
def generos_editar(id):
    data = request.json
    genero = Genero.query.get(id)
    genero.nombre = data['nombre']
    db.session.commit()
    return jsonify({
        "message": "Género actualizado"
    })

@app.route('/generos/<int:id>', methods=['DELETE'])
def generos_eliminar(id):
    genero = Genero.query.get(id)
    db.session.delete(genero)
    db.session.commit()
    return jsonify({
        "message": "Género eliminado"
    })

@app.route('/autores', methods=['GET'])
def autores_index():
    autores = Autor.query.all()
    # Creamos el contenido mediante una lista por comprensión
    data = [{'id':autor.id, 'nombre':autor.nombres, 'nacionalidad':autor.nacionalidad, 'fecha_nacimiento': autor.fecha_nacimiento} for autor in autores]
    return jsonify(data)

@app.route('/autores', methods=['POST'])
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

@app.route('/autores/<int:id>', methods=['GET'])
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

@app.route('/autores/<int:id>', methods=['PUT'])
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

@app.route('/autores/<int:id>', methods=['DELETE'])
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
