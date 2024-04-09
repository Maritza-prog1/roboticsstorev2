from flask import Flask, render_template, request, redirect, url_for
import daousuarios, os,daoComponentes
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER ="/img"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER

@app.route('/')
def index():
   return render_template('index.html')

@app.route("/registroUser",methods=["POST","GET"])
def registroUser():
   if request.method == 'POST':
      nomUser = request.form['nomUser']
      password = request.form['password']
      privilegios	= request.form['privilegios']
      daousuarios.insertarUsuario(nomUser, password, privilegios)
      return redirect(url_for('cs'))
   return render_template("registroUser.html")

@app.route("/cs")
def cs():
   cs = daousuarios.obtenerUsuario()
   return render_template('cs.html',cs=cs)

@app.route("/eliminarUser/<int:idUser>")
def eliminarUser(idUser):
   daousuarios.eliminarUsuario(idUser)
   return redirect(url_for('cs'))

@app.route("/actualizarUser",methods=['POST','GET'])
def actualizarUser():
   if request.method == 'POST':
      idUser = request.form['idUser']
      nomUser = request.form['nomUser']
      password = request.form['password']
      privilegios	= request.form['privilegios']
      daousuarios.editarUser(idUser,nomUser,password,privilegios)
      return redirect(url_for('cs'))

@app.route("/editarUser/<int:idUser>")
def editarUser(idUser):
    usuario = daousuarios.obteneridUser(idUser)
    return render_template("editarUser.html",usuario=usuario)

@app.route("/registroComponentes",methods=["POST","GET"])
def registroComponentes():
   if request.method == 'POST':
      nombreComponente = request.form['nombreComponente']
      caracteristicas = request.form['caracteristicas']
      precioUnitario	= request.form['precioUnitario']
      cantidad	= request.form['cantidad']
      imagen	= request.form['imagen']
      tipo	= request.form['tipo']
      daoComponentes.insertarComponentes(nombreComponente, caracteristicas, precioUnitario,cantidad,imagen,tipo)
      return redirect(url_for('listaComponentes'))
   return render_template("registroComponentes.html")

@app.route("/listaComponentes")
def listaComponentes():
   componentes = daoComponentes.obtenerComponentes()
   return render_template('listaComponentes.html',componentes=componentes)

@app.route("/actualizarComponente",methods=['POST','GET'])
def actualizarComponente():
   if request.method == 'POST':
      idcomponente = request.form['idcomponente']
      nombreComponente = request.form['nombreComponente']
      caracteristicas = request.form['caracteristicas']
      precioUnitario = request.form['precioUnitario']
      cantidad = request.form['cantidad']
      imagen = request.form['imagen']
      tipo = request.form['tipo']
      daoComponentes.editarComponente(idcomponente,nombreComponente,caracteristicas,precioUnitario,cantidad,imagen,tipo)
      return redirect(url_for('listaComponentes'))

@app.route("/editarComponente/<int:idcomponente>")
def editarComponente(idcomponente):
    componente = daoComponentes.obteneridcomponente(idcomponente)
    return render_template("editarComponente.html",componente=componente)

@app.route("/eliminarComponente/<int:idcomponente>")
def eliminarComponente(idcomponente):
   daoComponentes.eliminarComponente(idcomponente)
   return redirect(url_for('listaComponentes'))

@app.route("/sensores")
def sensores():
   componentes = daoComponentes.obtenerComponentes()
   return render_template('sensores.html',componentes=componentes)

@app.route("/motores")
def motores():
   componentes = daoComponentes.obtenerComponentes()
   return render_template('motores.html',componentes=componentes)

@app.route("/arduinos")
def arduinos():
   componentes = daoComponentes.obtenerComponentes()
   return render_template('arduinos.html',componentes=componentes)

@app.route("/TTL")
def TTL():
   componentes = daoComponentes.obtenerComponentes()
   return render_template('TTL.html',componentes=componentes)

@app.route("/CPLD")
def CPLD():
   componentes = daoComponentes.obtenerComponentes()
   return render_template('CPLD.html',componentes=componentes)

if __name__ == "__main__":
   app.run(port=7000)