from flask import Flask
from flask import render_template
from flask import request
from jinja2 import Template

comentarios_vulnerables = [("Perico", "¡Este formulario es vulnerable!")]
comentarios_seguros = [("Perico", "Este formulario es seguro :)")]
                
comentarios_vulnerables = []
comentarios_seguros = []


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")    

@app.route("/xss", methods=["GET", "POST"])
def xss(vuln=None):
    if (request.method == 'POST'):
        usuario = "Anonimo"
        try:
            comentarios_seguros.append(("Anonimo", request.form["formulario_seguro"]))
        except:
            pass
        try:
            comentarios_vulnerables.append(("Anonimo", request.form["formulario_vulnerable"]))
        except:
            pass
    return render_template("xss.html", coments_seguros=comentarios_seguros, coments_vulnerables=comentarios_vulnerables)


@app.route("/sql ", methods=["GET", "POST"])
def sql():
    pass

    

