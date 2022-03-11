from flask import Flask, render_template, request, url_for, redirect
from forms import formulario

app = Flask(__name__)

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
		return redirect(url_for('index'))
	
	else:
		return render_template("contacto.html", form=form)


if __name__ == '__main__':
	app.run(debug=True)

