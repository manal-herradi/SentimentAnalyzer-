# Prétraitement des données
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def load_data():
    data = pd.read_csv('data/data_sentiments.csv', encoding='ISO-8859-1')
    data['selected_text'] = data['selected_text'].apply(preprocess_text)
    return data

def preprocess_text(text):
    # Convertir en minuscules et diviser le texte en mots
    text = str(text)
    words = text.lower().split() 
    # Supprimer les mots vides 
    # "Mots courants qui n’apportent pas de valeur significative à l’analyse du texte
    # comme "le", "de", "et", "à", "the", "is", "in", "on""
    words = [word for word in words if word not in stop_words]
    # Rejoindre les mots nettoyés en une seule chaîne de texte
    return ' '.join(words)