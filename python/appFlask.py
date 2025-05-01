from flask import Flask

# Créer l'application Flask
app = Flask(__name__)

# Définir une route pour la page d'accueil
@app.route('/')
def home():
    return "Hello, Docker World!"

# Lancer l'application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)