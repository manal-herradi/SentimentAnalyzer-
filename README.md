# Analyse des Sentiments dans les Avis Clients (NLP)

Ce projet permet d'analyser les sentiments des avis clients en temps réel à l'aide des techniques de traitement du langage naturel (NLP). Les avis sont classifiés en trois catégories : positifs, négatifs, ou neutres. Le modèle utilise des techniques avancées de machine learning et est exposé via une API Flask.

## Technologies utilisées

- **Backend** : Flask (API REST)
- **Machine Learning** : Scikit-learn, NLTK, Spacy
- **Base de données** : PostgreSQL
- **Frontend** : HTML, CSS, JavaScript (interface pour soumettre les avis)
- **Environnement de développement** : Python 3, Virtualenv

## Fonctionnalités

- **Analyse des sentiments** : Classifie les avis clients en positifs, négatifs ou neutres à l'aide de modèles de machine learning.
- **Interface web** : Permet aux utilisateurs d'entrer des avis sous forme de texte et de recevoir l'analyse des sentiments en retour.
- **API Flask** : L'API expose le modèle de machine learning et permet de soumettre des avis via des requêtes HTTP.
- **Stockage des avis** : Les avis sont stockés dans une base de données PostgreSQL pour un traitement et une analyse continue.

## Installation

### Prérequis

1. **Python 3** et **pip** doivent être installés sur votre machine.
2. Installez les dépendances nécessaires en exécutant :
    ```bash
    pip install -r requirements.txt
    ```

### Démarrer l'application

1. Clonez ce repository :
    ```bash
    git clone https://github.com/manal-herradi/SentimentAnalyzer-.git
    cd analyse-sentiments
    ```

2. Activez un environnement virtuel :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Linux/MacOS
    venv\Scripts\activate  # Sur Windows
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Exécutez le serveur Flask :
    ```bash
    python app.py
    ```

    L'application sera accessible à `http://127.0.0.1:5000/`.

5. L'API Flask est également accessible à `http://127.0.0.1:5000/api/analyse_sentiment`.

## Utilisation de l'API

Pour analyser un avis, envoyez une requête POST à l'API avec le texte de l'avis. Exemple avec `curl` :

```bash
curl -X POST http://127.0.0.1:5000/api/analyse_sentiment \
    -H "Content-Type: application/json" \
    -d '{"avis": "Ce produit est excellent, je le recommande !"}'
```

Réponse attendue :
```json
{
  "sentiment": "positif"
}
```

## Structure du projet

```
analyse-sentiments/
│
├── app.py                  # Point d'entrée de l'application Flask
├── models/                 # Dossier contenant les scripts de formation du modèle
│   ├── model.py            # Entraînement et stockage du modèle de ML
│   └── preprocess.py       # Prétraitement des données (nettoyage, tokenisation)
├── static/                 # Dossier pour les fichiers statiques (CSS, JS)
│   └── styles.css          # Fichier CSS pour l'interface
├── templates/              # Dossier pour les templates HTML
│   └── index.html          # Page d'accueil avec formulaire d'entrée d'avis
├── requirements.txt        # Liste des dépendances Python
└── README.md               # Documentation du projet
```
