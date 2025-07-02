# keep_alive.py
from flask import Flask
from threading import Thread

# ➜ Crée une instance Flask
app = Flask('')

# ➜ Route principale pour montrer que ton bot est en vie
@app.route('/')
def home():
    return "✅ Ton bot est bien en ligne !"

# ➜ Fonction pour lancer le serveur web
def run():
    app.run(host='0.0.0.0', port=8080)

# ➜ Fonction pour démarrer le serveur dans un thread séparé
def keep_alive():
    server = Thread(target=run)
    server.start()
