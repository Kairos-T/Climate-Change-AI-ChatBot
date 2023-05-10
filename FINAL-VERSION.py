import random
import string

import nltk
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models, similarities

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Sample responses to different intents (Read Info for more clarity)
GREETINGS = ["Hello!", "Hi there!", "Greetings!", "Hey!"]
GOODBYES = ["Goodbye!", "See you later!", "Bye!", "Have a nice day!"]
AFFIRMATIONS = ["Okay", "Got it", "Sure", "Yes"]
NEGATIONS = ["No", "Not really", "Sorry"]
CLIMATE_INFO = ["Climate change is caused by human activities, such as burning fossil fuels and deforestation.",
                "Global warming is the long-term warming of the planet's overall temperature.",
                "Rising temperatures are causing more frequent and severe weather patterns, such as heat waves and hurricanes.",
                "Reducing your carbon footprint by conserving energy and resources is one way to combat climate change."]

# Sample questions to prompt user for input 
GREETINGS_PROMPT = ["Hello! How can I assist you today?", "Hi there! What can I help you with?", "Greetings! What brings you here?"]
HELP_PROMPT = ["What do you need help with?", "How can I assist you?", "What can I help you with today?"]
CLIMATE_PROMPT = ["Do you have any questions about climate change?", "What would you like to know about climate change?",
                  "Can I provide you with any information on climate change?"]

# Responses based on user input (Info for more clarity)
RESPONSES = {
    "greetings": GREETINGS,
    "goodbyes": GOODBYES,
    "affirmations": AFFIRMATIONS,
    "negations": NEGATIONS,
    "climate_info": CLIMATE_INFO
}

# Preprocess text
def preprocess_text(text):
    # Tokenize text
    tokens = nltk.word_tokenize(text.lower())
    # Remove punctuation
    tokens = [token for token in tokens if token not in string.punctuation]
    # Lemmatize tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

# Create dictionary and corpus
texts = CLIMATE_INFO
texts = [preprocess_text(text) for text in texts]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Create tf-idf model
tfidf = models.TfidfModel(corpus)

# Create index
index = similarities.MatrixSimilarity(tfidf[corpus])

# Generate response
def generate_response(user_input):
    # Preprocess user input
    input_tokens = preprocess_text(user_input)
    # Create tf-idf vector
    input_bow = dictionary.doc2bow(input_tokens)
    input_tfidf = tfidf[input_bow]
    # Get similarities
    similarities = index[input_tfidf]
    # Find closest match
    closest_match_index = similarities.argmax()
    # Return response
    return CLIMATE_INFO[closest_match_index]

# X Start X
print("Welcome to the Climate Change Education Chatbot! How can I assist you today?")
user_response = input()

# Process user input and generate chatbot response
while user_response.lower() != "bye":
    response = generate_response(user_response)
    print(response)

    if response in GREETINGS:
        print(random.choice(GREETINGS_PROMPT))
    elif response in HELP_PROMPT:
        print(random.choice(HELP_PROMPT))

import gensim
from gensim import corpora, models, similarities

dictionary = corpora.Dictionary(RESPONSES.values())
corpus = [dictionary.doc2bow(text) for text in RESPONSES.values()]
tfidf = models.TfidfModel(corpus)

def generate_response(user_input):
    # Clean and tokenize user input
    input_tokens = nltk.word_tokenize(user_input.lower())
    input_tokens = [lemmatizer.lemmatize(token) for token in input_tokens if token not in string.punctuation]

    # Check for keyword matches in input
    for intent, keywords in KEYWORDS.items():
        for keyword in keywords:
            if keyword in input_tokens:
                return random.choice(RESPONSES[intent])

    # If no keyword matches, generate response based on similarity to previous inputs
    vec_bow = dictionary.doc2bow(input_tokens)
    vec_tfidf = tfidf[vec_bow]
    index = similarities.MatrixSimilarity(tfidf[corpus])
    sims = index[vec_tfidf]
    closest_match_index = sims.argmax()
    return RESPONSES["generic"][closest_match_index]
