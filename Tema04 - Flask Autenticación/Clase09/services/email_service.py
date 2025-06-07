from flask_mail import Message
from extensions import mail

def enviarCorreo(asunto, desde, destino, mensaje_texto, mensaje_html):
    mensaje = Message(asunto)
    mensaje.sender=desde
    mensaje.recipients=destino
    mensaje.body = mensaje_texto
    mensaje.html = mensaje_html
    mail.send(mensaje)
