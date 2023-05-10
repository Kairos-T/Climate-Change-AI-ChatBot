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
                "Reducing your carbon footprint by conserving energy and resources is one way to combat climate change."
                "Climate change is caused by human activities, such as burning fossil fuels and deforestation.",
                "The Earth's temperature is rising due to greenhouse gas emissions from human activities.",
                "The effects of climate change include rising sea levels, more frequent extreme weather events, and loss of biodiversity.",
                "Reducing carbon emissions and transitioning to renewable energy sources are important steps in combating climate change.",
                "Individual actions, such as using energy-efficient appliances and reducing meat consumption, can also help mitigate climate change."
                "Climate change is causing shifts in weather patterns, resulting in longer and more severe droughts, heat waves, and floods.",
                "Melting ice caps are causing sea levels to rise, which threatens to flood low-lying areas and displace millions of people.",
                "The changing climate is affecting wildlife, causing some species to migrate to new areas or struggle to survive.",
                "Scientists have predicted that without action to address climate change, global temperatures could rise by several degrees Celsius by the end of the century.",
                "Climate change is a global problem that requires coordinated international action to address."
                "The Arctic sea ice is melting at a rate of 12.8% per decade."
                "The global sea level has risen about 8 inches since 1880, with almost half of that rise occurring in the last 25 years."
                r"The ocean has absorbed 93% of the extra heat from greenhouse gas emissions since the 1970s, leading to warmer and more acidic waters."
                "Carbon dioxide concentration in the atmosphere has reached 419 parts per million, the highest level in at least 800,000 years."
                "The world's glaciers are shrinking at an accelerated pace, losing 267 billion metric tons of ice per year on average between 2000 and 2019."
                "Climate change is exacerbating wildfires, making them more frequent and intense."
                "Climate change is causing more frequent and severe heat waves, which can lead to heat exhaustion and other health problems."
                r"The ocean's acidity has increased by 30% since the Industrial Revolution, making it harder for shellfish and other marine organisms to survive."
                "Climate change is causing coral reefs to bleach and die off, leading to the loss of biodiversity in marine ecosystems."
                "Climate change is causing more frequent and intense hurricanes and cyclones, leading to greater destruction and loss of life."
                "Climate change is causing more frequent and intense flooding, displacing millions of people each year."
                "Climate change is causing disruptions in global food production, with yields of staple crops like wheat and maize projected to decline in many regions."
                "Climate change is exacerbating water scarcity in many parts of the world, with an estimated 1.8 billion people living in areas with inadequate water supply."
                "Climate change is causing the migration and extinction of many species, disrupting entire ecosystems."
                "Climate change is projected to cost the global economy trillions of dollars in damages and lost productivity over the next century."
]

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
    climate_responses = [
        "Climate change is caused by human activities, such as burning fossil fuels and deforestation.",
        "The Earth's temperature is rising due to greenhouse gas emissions from human activities.",
        "The effects of climate change include rising sea levels, more frequent extreme weather events, and loss of biodiversity.",
        "Reducing carbon emissions and transitioning to renewable energy sources are important steps in combating climate change.",
        "Individual actions, such as using energy-efficient appliances and reducing meat consumption, can also help mitigate climate change."
        "Climate change is causing shifts in weather patterns, resulting in longer and more severe droughts, heat waves, and floods.",
        "Melting ice caps are causing sea levels to rise, which threatens to flood low-lying areas and displace millions of people.",
        "The changing climate is affecting wildlife, causing some species to migrate to new areas or struggle to survive.",
        "Scientists have predicted that without action to address climate change, global temperatures could rise by several degrees Celsius by the end of the century.",
        "Climate change is a global problem that requires coordinated international action to address."
        "The Arctic sea ice is melting at a rate of 12.8% per decade."
        "The global sea level has risen about 8 inches since 1880, with almost half of that rise occurring in the last 25 years."
        r"The ocean has absorbed 93% of the extra heat from greenhouse gas emissions since the 1970s, leading to warmer and more acidic waters."
        "Carbon dioxide concentration in the atmosphere has reached 419 parts per million, the highest level in at least 800,000 years."
        "The world's glaciers are shrinking at an accelerated pace, losing 267 billion metric tons of ice per year on average between 2000 and 2019."
        "Climate change is exacerbating wildfires, making them more frequent and intense."
        "Climate change is causing more frequent and severe heat waves, which can lead to heat exhaustion and other health problems."
        r"The ocean's acidity has increased by 30% since the Industrial Revolution, making it harder for shellfish and other marine organisms to survive."
        "Climate change is causing coral reefs to bleach and die off, leading to the loss of biodiversity in marine ecosystems."
        "Climate change is causing more frequent and intense hurricanes and cyclones, leading to greater destruction and loss of life."
        "Climate change is causing more frequent and intense flooding, displacing millions of people each year."
        "Climate change is causing disruptions in global food production, with yields of staple crops like wheat and maize projected to decline in many regions."
        "Climate change is exacerbating water scarcity in many parts of the world, with an estimated 1.8 billion people living in areas with inadequate water supply."
        "Climate change is causing the migration and extinction of many species, disrupting entire ecosystems."
        "Climate change is projected to cost the global economy trillions of dollars in damages and lost productivity over the next century."

    ]
    
    goodbye_responses = [
        "Goodbye!",
        "Thanks for chatting. Goodbye!",
        "It was nice talking to you. Goodbye!",
        "See you later!",
        "Take care!"
    ]

    user_input = user_input.lower()

    if "climate" in user_input:
        return random.choice(climate_responses)
    elif "bye" in user_input:
        return random.choice(goodbye_responses)
    else:
        return "I'm sorry, I didn't understand what you were trying to say. Can you please rephrase?"
        
print("Hello! Let's talk about climate change.")
while True:
    user_input = input("You: ")
    response = generate_response(user_input)
    print("Bot:", response)
    if "bye" in user_input:
        break


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

