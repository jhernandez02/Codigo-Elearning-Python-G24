from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import db
from dotenv import load_dotenv
import os

# Importamos las rutas
from routes.usuarios import usuario_router

# Cargamos las variables desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config["JWT_SECRET_KEY"] = "super-secret"

# Inicializamos la aplicación
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Registramos las rutas
app.register_blueprint(usuario_router)

@app.route("/")
def hello_world():
    return "<p>Hola, Mundo!</p>"
