from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

class Genero(db.Model):
    __tablename__ = 'generos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),nullable=False)

class Autor(db.Model):
    __tablename__ = 'autores'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100),nullable=False)
    nacionalidad = db.Column(db.String(25))
    fecha_nacimiento = db.Column(db.Date)

class Libro(db.Model):
    __tablename__ = 'libros'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150),nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('autores.id'), nullable=False)
    genero_id = db.Column(db.Integer, db.ForeignKey('generos.id'), nullable=False)
    isbn = db.Column(db.String(25))
    estado = db.Column(db.String(12), default='Disponible', nullable=False) # 'Disponible','Prestado','Inactivo'
    # Creamos las relaciones
    autor = db.relationship('Autor')
    genero = db.relationship('Genero')

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    password_hash = db.Column(db.String(255),nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Prestamo(db.Model):
    __tablename__ = 'prestamos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    fecha_prestamo = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_devolucion = db.Column(db.DateTime)
    estado = db.Column(db.String(10), default='Activo', nullable=False) # 'Activo','Devuelto'

class PrestamoLibro(db.Model):
    __tablename__ = 'prestamo_libros'
    prestamo_id = db.Column(db.Integer, db.ForeignKey('prestamos.id'), primary_key=True)
    libro_id = db.Column(db.Integer, db.ForeignKey('libros.id'), primary_key=True)
