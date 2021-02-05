import nltk
nltk.download('punkt')

def get_num_sentences(text):
    sentences = nltk.tokenize.sent_tokenize(text)
    return len(sentences)

def get_num_words(text):
    sentences = nltk.tokenize.sent_tokenize(text)
    num_words = 0
    for sent in sentences:
        num_words+=len(sent.split())
    return num_words