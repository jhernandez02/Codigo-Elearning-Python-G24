from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from extensions import mail
from models import db
from dotenv import load_dotenv
import os

# Importamos las rutas
from routes.usuarios import usuario_router
from routes.password import password_router

# Cargamos las variables desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config["JWT_SECRET_KEY"] = "super-secret"

# Configuración del envío de correo
app.config['MAIL_SERVER']= os.getenv("MAIL_HOST")
app.config['MAIL_PORT'] = os.getenv("MAIL_PORT")
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USER")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASS")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Inicializamos la aplicación
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
mail.init_app(app)

# Registramos las rutas
app.register_blueprint(usuario_router)
app.register_blueprint(password_router)

@app.route("/")
def hello_world():
    return "<p>Hola, Mundo!</p>"
