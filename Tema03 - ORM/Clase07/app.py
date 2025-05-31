from flask import Flask
from flask_migrate import Migrate
from models import db
from dotenv import load_dotenv
import os

# Importamos las rutas
from routes.generos import genero_router
from routes.autores import autor_router
from routes.libros import libro_router

# Cargamos las variables desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

# Inicializamos la aplicación
db.init_app(app)
migrate = Migrate(app, db)

# Registramos las rutas
app.register_blueprint(genero_router)
app.register_blueprint(autor_router)
app.register_blueprint(libro_router)

@app.route("/")
def hello_world():
    return "<p>Hola, Mundo!</p>"
