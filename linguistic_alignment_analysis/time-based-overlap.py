#%% Imports
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet, stopwords
import nltk
from nltk.stem import WordNetLemmatizer


#%% Preprocessing functions for lexical word
def get_wordnet_pos(treebank_tag):
    """
    Converts a Treebank parts of speech (POS) tag to a Wordnet POS tag.
    :param treebank_tag: Treebank POS tag
    :return: Wordnet POS tag
    """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def preprocess_message_lexical_word(post):
    """
    Preprocesses text posts before applying Time-based overlap, by tokenizing, lowercasing and removing separate punctuation tokens.
    :param post: message to preprocess
    :return: preprocessed message: list of lemmas
    """
    # Tokenize post
    tokens = word_tokenize(post)
    # Remove tokens that exist solely of punctuation and remove stopwords
    stop_words = set(stopwords.words('english'))
    # post_punctuation_stopwords_removed = [token.lower() for token in tokens if token not in string.punctuation and token not in stop_words]
    post_stopwords_removed = [token.lower() for token in tokens if token not in stop_words]
    # Apply POS
    tagged = nltk.pos_tag(post_stopwords_removed)
    # Get lemmas
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word, tag in tagged:
        wntag = get_wordnet_pos(tag)
        if wntag is None:  # not supply tag in case of None
            lemmas.append(lemmatizer.lemmatize(word))
        else:
            lemmas.append(lemmatizer.lemmatize(word, pos=wntag))

    return lemmas