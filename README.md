# Analyse des Sentiments dans les Avis Clients (NLP)

Ce projet permet d'analyser les sentiments des avis clients en temps réel en anglais à l'aide des techniques de traitement du langage naturel (NLP). Les avis, rédigés en anglais, sont classifiés en trois catégories : positifs, négatifs, ou neutres. Le modèle utilise des techniques avancées de machine learning et est exposé via une API Flask.

## Technologies utilisées

- **Backend** : Flask (API REST)
- **Machine Learning** : Scikit-learn, NLTK, Spacy
- **Frontend** : HTML, CSS, JavaScript (interface pour soumettre les avis)
- **Environnement de développement** : Python 3, Virtualenv

## Fonctionnalités

- **Analyse des sentiments** : Classifie les avis clients en positifs, négatifs ou neutres à l'aide de modèles de machine learning.
- **Interface web** : Permet aux utilisateurs d'entrer des avis sous forme de texte et de recevoir l'analyse des sentiments en retour.
- **API Flask** : L'API expose le modèle de machine learning et permet de soumettre des avis via des requêtes HTTP.

## Sélection des Mots Pertinents

Il est important de sélectionner les mots utilisés dans le texte de manière pertinente afin d'optimiser la performance du modèle. Lors de la première phase d'entraînement, j'ai observé que les résultats étaient peu satisfaisants en raison de l'inclusion de mots non pertinents dans les avis. Après avoir sélectionné uniquement les mots les plus significatifs, la précision du modèle a considérablement augmenté, passant de 0,6 à 0,83. Cette sélection des mots a permis au modèle d'identifier plus efficacement les sentiments exprimés dans les avis clients.

## Installation

### Prérequis

- **Python 3** et **pip** doivent être installés sur votre machine.


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

5. L'API Flask est également accessible à `http://127.0.0.1:5000/analyze`.

## Utilisation de l'API

Pour analyser un avis, envoyez une requête POST à l'API avec le texte de l'avis. Exemple avec `curl` :

```bash
curl --request POST http://127.0.0.1:5000/analyze `
    --header "Content-Type: application/json" `
    --data '{"text": "This product is amazing, I recommend it!"}'
```

Réponse attendue :
```json
{
  "sentiment": "positive"
}
```

## Exemples de Résultats du Modèle 

### Sentiment Négatif

![Sentiment Négatif](https://github.com/manal-herradi/images/blob/859b0fc0e6ab747375d1bc8a3e1df17276e37173/negative.png)

### Sentiment Neutre
![Sentiment Neutre](https://github.com/manal-herradi/images/blob/859b0fc0e6ab747375d1bc8a3e1df17276e37173/Neutral.png)

### Sentiment Positif
![Sentiment Positif](https://github.com/manal-herradi/images/blob/859b0fc0e6ab747375d1bc8a3e1df17276e37173/Positive.png)

## Structure du projet

```
analyse-sentiments/
│
├── app.py                  # Point d'entrée de l'application Flask
├── models/                 # Dossier contenant les scripts de formation du modèle
│   ├── model.py            # Entraînement et stockage du modèle de ML
│   ├── preprocess.py       # Prétraitement des données (nettoyage, tokenisation)
|   ├── sentiment_model.pkl # Modèle entraîné pour la classification
|   └── vectorizer.pkl      # Vectorizer utilisé pour transformer les textes en représentations numériques avant l'entraînement du modèle !
├── static/                 # Dossier pour les fichiers statiques (CSS, JS)
│   └── styles.css          # Fichier CSS pour l'interface
├── templates/              # Dossier pour les templates HTML
│   └── index.html          # Page d'accueil avec formulaire d'entrée d'avis
├── requirements.txt        # Liste des dépendances Python
└── README.md               # Documentation du projet
```
