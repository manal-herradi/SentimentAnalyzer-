from flask import Flask, request, jsonify, render_template
from models.model import load_model, predict_sentiment

''' Flask est un framework web léger en Python qui permet de créer des applications web,
en définissant des routes et des vues pour gérer les requêtes HTTP'''

# Initialisation de l'application Flask
app = Flask(__name__)

# Charger le modèle et le vectoriseur
model, vectorizer = load_model()

# Définition des routes de l'API
@app.route('/')
def home():
    # "render_template" permet à Flask de chercher un fichier HTML dans le dossier templates/
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    if request.is_json:
        data = request.get_json()
        text = data.get('text', '')
        sentiment = predict_sentiment(text, model, vectorizer)
        return jsonify({'sentiment': sentiment}), 200
    return jsonify({'error': 'Request must be JSON'}), 400

if __name__ == "__main__":
    app.run(debug=True)