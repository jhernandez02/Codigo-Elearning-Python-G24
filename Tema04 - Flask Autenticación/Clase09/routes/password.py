from flask import Blueprint, request, jsonify
from cryptography.fernet import Fernet
from models import db, Usuario
from services.email_service import enviarCorreo
import datetime

password_router = Blueprint('password', __name__)

FERNET_SECRET_KEY = Fernet.generate_key()
print('FERNET_SECRET_KEY:', FERNET_SECRET_KEY)
fernet = Fernet(FERNET_SECRET_KEY)

def generate_reset_hash(email, expiration=3600):
    # Obtenemos el tiempo actual en segundos
    timestamp = int(datetime.datetime.utcnow().timestamp())+expiration
    data = f"{email}|{timestamp}".encode()
    print('data:', data)
    hash_code = fernet.encrypt(data) # Ciframos con Fernet 
    return hash_code.decode()

@password_router.route('/solicitud-recuperar-contrasena', methods=['POST'])
def solicitudRecuperarContrasena():
    data = request.json
    val_email = data['email']
    # SELECT * FROM usuarios WHERE email='lmendoza@mail.com' LIMIT 1;
    usuario = Usuario.query.filter_by(email=val_email).first()

    if not usuario:
        return jsonify({
            "message": "Email no encontrado"
        }), 404
    
    codigo_hash = generate_reset_hash(val_email)
    reset_url = f"http://localhost:5000/restablecer-contrasena/{codigo_hash}"
    print('reset_url:', reset_url)

    #Envío del codigo_hash por correo al usuario
    asunto = "Recuperación de contraseña"
    desde = "no-reply@codigo.edu.pe"
    destino = [val_email]
    mensaje = f"Haz clic en el siguiente enlace para restablecer tu contraseña: {reset_url}"
    html = f'Haz clic en el siguiente enlace para restablecer tu contraseña: <a href="{reset_url}">Clic aquí</a>'
    enviarCorreo(asunto,desde,destino,mensaje,html)

    return jsonify({
        "message": "Correo de recuperación enviado"
    })

def verify_reset_hash(code_hash):
    decrypted_data = fernet.decrypt(code_hash.encode()).decode()
    print('decrypted_data: ', decrypted_data)
    email, expiration_time = decrypted_data.split('|')

    expiration_time = int(expiration_time) # 11pm
    current_time = int(datetime.datetime.utcnow().timestamp()) # 10.57pm

    if expiration_time < current_time:
        return None

    return email

@password_router.route('/restablecer-contrasena', methods=['POST'])
def restablecerContrasena():
    data = request.json
    val_codigo = data['codigo']
    val_password = data['password']

    val_email = verify_reset_hash(val_codigo)

    usuario = Usuario.query.filter_by(email=val_email).first()

    if not usuario:
        return jsonify({
            "message": "Usuario no encontrado"
        }), 404
    
    usuario.set_password(val_password)
    db.session.commit()

    return jsonify({
        "message": "Contraseña actualizada correctamente"
    })
