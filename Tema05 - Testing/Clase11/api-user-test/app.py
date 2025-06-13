from flask import Flask, request, jsonify

app = Flask(__name__)

contId = 4

lista = [
    {'id':1, 'nombre':'Jhon','email':'jhon@mail.com','clave':'123456'},
    {'id':2, 'nombre':'Karen','email':'karen@mail.com','clave':'123456'},
    {'id':3, 'nombre':'Miguel','email':'miguel@mail.com','clave':'123456'},
]

# Ruta para crear usuarios
@app.route('/usuarios', methods=['POST'])
def usuario_crear():
    global contId
    data = request.get_json()
    encontrado = False
    try:
        nombre = data['nombre']
        email = data['email']
        clave = data['clave']
        for user in lista:
            if(user['email']==email):
                encontrado = True
                break
        if encontrado:
            return jsonify({
                'message': 'El usuario ya existe'
            }), 200
        else:
            lista.append({
                'id': contId,
                'nombre': nombre,
                'email': email,
                'clave': clave
            })
            contId = contId + 1
            return jsonify({
                'message': 'Usuario creado satisfactoriamente'
            }), 200
    except Exception as error:
        return jsonify({
            'message': 'No se pudo crear el usuario'
        }), 500

# Ruta para loguearse
@app.route('/login', methods=['POST'])
def usuario_login():
    data = request.get_json()
    encontrado = False
    try:
        email = data['email']
        clave = data['clave']
        for user in lista:
            if(user['email']==email and user['clave']==clave):
                encontrado = True
                break
        if encontrado:
            return jsonify({
                'message': 'Login satisfactorio'
            }), 200
        else:
            return jsonify({
                'message': 'Credenciales incorrectas'
            }), 400
    except Exception as error:
        return jsonify({
            'message': 'Ocurrió un error'
        }), 500

# Ruta para recuperar la contraseña
@app.route('/recuperar-contrasena', methods=['POST'])
def usuario_recuperar_contrasena():
    encontrado = False
    data = request.get_json()
    try:
        email = data['email']
        for user in lista:
            if(user['email']==email ):
                encontrado = True
                break
        if encontrado:
            return jsonify({
                'message': 'Contraseña reiniciada satisfactoriamente'
            }), 200
        else:
            return jsonify({
                'message': 'Usuario no encontrado'
            }), 400
    except Exception as error:
        return jsonify({
            'message': 'Ocurrió un error'
        }), 500