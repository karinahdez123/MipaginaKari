from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def url_principal():
	return render_template("templatedos.html", nombre="Karina", fecha="17 de  Mayo del 2021", direccion="Santa Teresa Calle Gto #24",
		telefono="4735609270", correo="karyhb123@hotmail.com")

@app.route("/about_me")
def about_me():
      return render_template("about_me.html")
@app.route("/familia")
def familia():
      return render_template("familia.html")


if __name__== "__main__":

	app.run(debug=True)

