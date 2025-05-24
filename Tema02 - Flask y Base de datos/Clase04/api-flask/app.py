from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/usuarios", methods=["GET"])
def usuarios_listar():
    return "usuarios listar"

@app.route("/usuarios", methods=["POST"])
def usuarios_crear():
    return "usuario crear"

@app.route("/usuarios/<int:id>", methods=["GET"])
def usuarios_detalle(id):
    # consulta a la BD
    return "usuarios detalle id:"+str(id)

@app.route("/usuarios/<int:id>", methods=["PUT"])
def usuarios_actualizar(id):
    # consulta a la BD
    return "usuarios actualizado id:"+str(id)

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def usuarios_eliminar(id):
    # consulta a la BD
    return "usuarios eliminado id:"+str(id)