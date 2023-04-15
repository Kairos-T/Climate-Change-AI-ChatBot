import random

# defining some responses for the chatbot
greetings = ['hi', 'hello', 'hey', 'hola', 'welcome']
questions = ['what is climate change?', 'how does climate change affect the environment?', 'what can I do to help fight climate change?']
goodbyes = ['goodbye', 'bye', 'see you later', 'take care']

# define a function to generate a random response
def get_response(input_text):
    input_text = input_text.lower()
    
    if input_text in greetings:
        return random.choice(greetings).capitalize() + "! How can I help you learn about climate change?"
    
    elif input_text in questions:
        return "Climate change refers to the long-term changes in the Earth's climate. These changes are primarily caused by human activities such as the burning of fossil fuels, deforestation, and industrial processes. Climate change can lead to rising sea levels, more frequent natural disasters, and harm to wildlife and ecosystems. There are many ways you can help fight climate change, such as reducing your energy consumption, using public transportation, and supporting sustainable practices in your community."
    
    # if the user says goodbye
    elif input_text in goodbyes:
        return random.choice(goodbyes).capitalize() + "! Take care and stay eco-friendly!"
    
    # if the user says something else
    else:
        return "I'm sorry, I don't understand. Can you please ask me a question about climate change?"

# define a function to start the chatbot
def start_chatbot():
    print("Hi! I'm your climate change education chatbot. Ask me a question and I'll do my best to help you learn about climate change. If you want to exit, type 'bye'.")
    while True:
        user_input = input()
        if user_input.lower() == 'bye':
            print(get_response(user_input))
            break
        else:
            print(get_response(user_input))

# call the function to start the chatbot
start_chatbot()

#Extremely limited functionalities, only 3 questions that the bot can answer.
