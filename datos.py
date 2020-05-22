from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("index.html",info = "Alejandro", info2 = "student", info3 = "player")

@app.route("/entradas")
def url_entradas():
	return render_template("entradas.html",info = "Alejandro", info2 = "student", info3 = "player")

@app.route("/presentacion")
def url_presentacion():
	return render_template("template_info.html", info = "Alejandro", info2 = "student", info3 = "player", img = "alex.jpg", img2 = "xbox.png", cuenta = "Xbox", desc = "AlejandroX13358", img3 = "lol.png", cuenta2 = "League of Legends (LAN)", desc2 = "thenewAX13", img4 = "cod.png", cuenta3 = "CoD: Modern Warfare", desc3 = "Activision ID: thenewAX13#2441643\nO por gamertag de xbox", img5 = "epic.png", cuenta4 = "Epic Games (Fortnite)", desc4 = "thenewAX13", img6 = "steam.png", cuenta5 = "Steam", desc5 = "thenewAX13", img7 = "discord.png", cuenta6 = "Discord", desc6 = "thenewAX13#8986")

@app.route("/mi-vida-en-lol")
def url_exp_lol():
	return render_template("exp_lol.html",info = "Alejandro", info2 = "jugador toxico", info3 = "jg, mid y top")

@app.route("/mi-vida-en-fortnite")
def url_exp_fort():
	return render_template("exp_fort.html",info = "Alejandro", info2 = "manco", info3 = "noob")

if __name__ == "__main__":
	app.run(debug=True)