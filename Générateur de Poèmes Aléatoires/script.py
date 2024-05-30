import random
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return set(synonyms)

def get_rhyming_words(word):
    # This function would ideally use a rhyming dictionary API or dataset
    # For simplicity, it returns a list of made-up rhyming words
    return [word + ending for ending in ['ay', 'ay', 'ee', 'ow', 'igh']]

def generate_line(keywords):
    words = []
    for word in keywords:
        synonyms = get_synonyms(word)
        if synonyms:
            words.append(random.choice(list(synonyms)))
        else:
            words.append(word)
    return ' '.join(words)

def generate_poem(title, keywords):
    poem = []
    poem.append(title)
    poem.append('')
    for _ in range(4):  # Create a 4-line stanza
        line = generate_line(keywords)
        poem.append(line.capitalize())
    return '\n'.join(poem)

if __name__ == "__main__":
    title = "The Mysterious Forest"
    keywords = ['tree', 'whisper', 'shadow', 'dream']
    poem = generate_poem(title, keywords)
    print(poem)
