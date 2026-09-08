from flask import Flask, render_template, request, redirect
from funcao_grafico import grafico
from flask_sqlalchemy import SQLAlchemy
from banco import *
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]   =   "sqlite:///banco.db"
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")




@app.route("/form_euler", methods=["GET", "POST"])
def formulario_euler():
    if request.method == "POST":

        beta = request.form.get("beta")
        tempo = request.form.get("tempo")


        adicionado = Banco(beta=beta, tempo=tempo)

        
        db.session.add(adicionado)
        db.session.commit()


    return render_template("form_euler.html")



@app.route("/form_analitico", methods=['GET','POST'])
def formulario_analitico():
    return render_template("form_analitico.html")




@app.route('/form_ambos', methods=['GET', 'POST'])
def formulario_ambos():
    return render_template('form_ambos.html')


@app.route('/ver_graficos')
def visualizar_graficos():
    return render_template('ver_graficos.html')

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

