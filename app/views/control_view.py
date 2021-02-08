from flask import render_template, request, redirect, url_for
from app import app
from app.services import download_nome
from app.services import download_link
from app.services import download_video

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/musica-nome", methods=['GET','POST'])
def musica_nome():
    if request.method == 'POST':
        texto = request.form['texto']
        download_nome.campo_entry = texto
        download_nome.Download_nome()
        
        return redirect(url_for('home'))
    return render_template('musica_nome.html')

@app.route("/musica-link", methods=['GET','POST'])
def musica_link():
    if request.method == 'POST':
        texto = request.form['texto']
        download_link.campo_entry = texto
        download_link.Download_link()

        return redirect(url_for('home'))
    return render_template('musica_link.html')

@app.route("/video-link", methods=['GET','POST'])
def video_link():
    if request.method == 'POST':
        texto = request.form['texto']
        download_video.url = texto
        download_video.Download_Video()

        return redirect(url_for('home'))
    return render_template('video_download.html')