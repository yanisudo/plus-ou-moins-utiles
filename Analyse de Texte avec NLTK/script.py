import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Télécharger les ressources nécessaires de NLTK
nltk.download('punkt')
nltk.download('stopwords')

def analyze_text(text):
    # Tokenization
    words = word_tokenize(text)
    
    # Supprimer les stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    return filtered_words

if __name__ == "__main__":
    text = "Here is a simple example of text analysis using NLTK."
    filtered_words = analyze_text(text)
    print(filtered_words)
