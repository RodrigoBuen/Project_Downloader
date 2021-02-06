from flask import render_template, request, redirect, url_for
from app import app
from app.services import musica_nome

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/musica-nome", methods=['GET','POST'])
def musica_nome():
    if request.method == 'POST':
        texto = request.form['texto']
        musica_nome.campo_entry = texto
        musica_nome.Download()
        
        return redirect(url_for('home'))
    return render_template("musica_nome.html")

@app.route("/musica-link")
def musica_link():
    return render_template("musica_link.html")