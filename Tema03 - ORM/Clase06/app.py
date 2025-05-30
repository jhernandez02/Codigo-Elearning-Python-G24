from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Genero
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