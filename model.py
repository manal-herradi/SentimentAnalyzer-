from sklearn.model_selection import train_test_split
# Pour convertir du texte en vecteurs numériques
from sklearn.feature_extraction.text import CountVectorizer  
# Algorithme de classification
from sklearn.naive_bayes import MultinomialNB  
# Pour sauvegarder et charger le modèle
import pickle 
# Fonction qui charge et prétraite les données définit dans le fichier "preprocess.py"
# . to refer to the current directory :)
from .preprocess import load_data 
from sklearn.metrics import accuracy_score, classification_report


def train_model():
    data = load_data()
    texts = data['selected_text']
    labels = data['sentiment']
    
    # Transformer le texte en vecteurs numériques
    vectorizer = CountVectorizer()
    # Chaque mot est transformé en un indice !
    X = vectorizer.fit_transform(texts)

    # Division 70% train / 30% test
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3)
    
    # Entraînement du modèle Naïve Bayes sur les données
    model = MultinomialNB()
    model.fit(X_train, y_train)
    
    # Sauvegarde du modèle et du vectoriseur
    pickle.dump(model, open('models/sentiment_model.pkl', 'wb'))
    # Si on sauvegarde pas : Le modèle ne reconnaît pas les bons indices et donne des résultats incohérents
    pickle.dump(vectorizer, open('models/vectorizer.pkl', 'wb'))

    # Test du modèle et évaluation des performances
    y_pred = model.predict(X_test)
    
    # Calcul des scores d'accuracy et génération d'un rapport de classification
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    # Sauvegarde des résultats dans un fichier .txt
    with open('models/model_performance.txt', 'w') as file:
        file.write(f"Accuracy: {accuracy}\n\n")
        file.write(f"Classification Report:\n{report}")

def load_model():
    model = pickle.load(open('models/sentiment_model.pkl', 'rb'))
    vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))
    return model, vectorizer

def predict_sentiment(text, model, vectorizer):
    X = vectorizer.transform([text])
    return model.predict(X)[0]

if __name__ == "__main__":
    train_model()