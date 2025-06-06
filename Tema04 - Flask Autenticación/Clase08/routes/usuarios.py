from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from models import db, Usuario

usuario_router = Blueprint('usuarios', __name__)

@usuario_router.route('/registro', methods=['POST'])
def registrar():
    data = request.json
    nombre = data['nombre']
    usuario = data['email']
    passwd = data['passwd']
    # Validamos que se envien los valores
    if not usuario or not passwd:
        return jsonify({
            "message": "Usuario y contraseña son requeridos"
        })
    # Verificamos por el email si el usuario 
    if Usuario.query.filter_by(email=usuario).first():
        return jsonify({
            "message": "El usuario ya existe"
        })
    # Creamos un nuevo usuario
    nuevo_usuario = Usuario(nombre=nombre, email=usuario)
    nuevo_usuario.set_password(passwd)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({
        "message": "Usuario registrado exitosamente"
    })

@usuario_router.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    passwd = data['passwd']
    # Buscamos un usuario por el campo email
    usuario = Usuario.query.filter_by(email=email).first()
    # Validamos si el usuario NO existe o la contraseña es incorrecta
    if not usuario or not usuario.check_password(passwd):
        return jsonify({
            "message": "Credenciales incorrectas"
        })
    # Generamos el token de acceso
    token = create_access_token(identity=str(usuario.id))
    return jsonify({
        "token": token
    })

# Ruta protegida
@usuario_router.route('/datos', methods=['POST'])
@jwt_required()
def datos():
    data = request.json
    id = data['id']
    # Buscamos un usuario por el campo email
    usuario = Usuario.query.filter_by(id=id).first()
     # Validamos si el usuario NO existe
    if not usuario:
        return jsonify({
            "message": "El valor del id es inválido"
        })
    else:
        return jsonify({
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
        })

@usuario_router.route('/datos', methods=['GET'])
@jwt_required()
def getDatos():
    data = get_jwt_identity() # obtenemos el id del usuario
    usuario = Usuario.query.filter_by(id=data).first()
    return jsonify({
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email,
    })
    