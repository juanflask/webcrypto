import sqlite3
from flask import Flask, render_template, request, url_for, redirect
from forms import formulario

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

def get_db_connection():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite3.Row
	return conn

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
	form = formulario(request.form)
	if request.method == "POST":
		nombre= form.name.data
		email= form.email.data
		text=  form.text.data
		print(nombre + email + text)

		conn = get_db_connection()
		conn.execute('INSERT INTO contacto (nombre, email, mensaje) VALUES (?,?,?)',
			(nombre, email, text))
		conn.commit()
		conn.close()

		return redirect(url_for('index'))
	
	else:
		return render_template("contacto.html", form=form)


@app.route("/mensajes")
def mensajes():
	conn = get_db_connection()
	mensajes = conn.execute('SELECT * FROM contacto').fetchall()
	conn.close()
	return render_template('mensajes.html', mensajes=mensajes)

@app.route("/articulos")
def articulos():
	conn = get_db_connection()
	articulos = conn.execute('SELECT * FROM articulos').fetchall()
	conn.close()
	return render_template('articulos.html', articulos=articulos)

if __name__ == '__main__':
	app.run(debug=True)

