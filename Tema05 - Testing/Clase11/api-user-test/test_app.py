import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Configuramos el entorno de pruebas
        self.app = app.test_client()
        self.app.testing = True
    
    def test_usuario_crear(self):
        datos = {
            "nombre": "Javier Morales",
            "email": "javier@mail.com",
            "clave": "123456"
        }
        response = self.app.post('/usuarios', json=datos)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"message":"Usuario creado satisfactoriamente"}\n')
    
    def test_usuario_existente(self):
        datos = {
            "nombre": "Jhon Morales",
            "email": "jhon@mail.com",
            "clave": "123456"
        }
        response = self.app.post('/usuarios', json=datos)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"message":"El usuario ya existe"}\n')
    
    def test_usuario_error(self):
        datos = {
            "email": "jhon@mail.com",
            "clave": "123456"
        }
        response = self.app.post('/usuarios', json=datos)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, b'{"message":"No se pudo crear el usuario"}\n')
    
    def test_login_ok(self): # Escenario: Login satisfactorio
        datos = {
            "email": "jhon@mail.com",
            "clave": "123456"
        }
        response = self.app.post('/login', json=datos)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"message":"Login satisfactorio"}\n')
    
    def test_not_login(self): # Escenario: El usuario ya existe
        datos = {
            "email": "carlos@mail.com",
            "clave": "987654"
        }
        response = self.app.post('/login', json=datos)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"message":"Credenciales incorrectas"}\n')
    
    def test_login_error(self): # Escenario: Se genera un error
        datos = {
            "usuario": "carlos@mail.com",
            "clave": "987654"
        }
        response = self.app.post('/login', json=datos)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, b'{"message":"Ocurri\\u00f3 un error"}\n')
    
    def test_recuperar_contrasena_ok(self): # Escenario: Se reinicia la contraseña satisfactoriamente
        datos = {
            "email": "jhon@mail.com",
            "clave": "987654"
        }
        response = self.app.post('/recuperar-contrasena', json=datos)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"message":"Contrase\\u00f1a reiniciada satisfactoriamente"}\n')

    def test_recuperar_contrasena_not_ok(self): # Escenario: Usuario no existe
        datos = {
            "email": "alejandro@mail.com",
            "clave": "987654"
        }
        response = self.app.post('/recuperar-contrasena', json=datos)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"message":"Usuario no encontrado"}\n')

    def test_recuperar_contrasena_error(self): # Escenario: Se genera un error:
        datos = {
            "usuario": "carlos@mail.com",
            "clave": "987654"
        }
        response = self.app.post('/login', json=datos)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, b'{"message":"Ocurri\\u00f3 un error"}\n')
