import random

# Defines a list of climate change facts and responses
facts = ["Global temperatures are rising at a rate faster than ever before.",
         "The 20 hottest years on record have occurred since 1981.",
         "The Arctic ice is melting at a rate of 9% per decade.",
         "The amount of carbon dioxide in the atmosphere has increased by 40% since the start of the Industrial Revolution.",
         "Oceans have absorbed 93% of the excess heat caused by greenhouse gas emissions.",
         "Climate change is causing more extreme weather events, such as hurricanes, heatwaves, and droughts.",
         "Sea levels have risen 8 inches on average since 1880.",
         "97% of climate scientists agree that climate-warming trends over the past century are very likely due to human activities."]

responses = ["That's interesting. Tell me more!",
             "Wow, I didn't know that. Thanks for sharing!",
             "How do you think we can help combat climate change?",
             "I completely agree. It's important that we take action to address climate change.",
             "Do you have any ideas for how we can reduce our carbon footprint?"]

# Defines a function to generate a response based on user input
def get_response(user_input):
    if "climate change" in user_input:
        return random.choice(responses)
    elif "fact" in user_input:
        return random.choice(facts)
    elif "help" in user_input:
        return "I can provide you with facts about climate change or we can discuss how we can help combat it. What would you like to do?"
    else:
        return "I'm sorry, I didn't understand. Can you please rephrase your question?"

# Defines the main function to run the chatbot
def main():
    print("Welcome to the Climate Change Chatbot! How can I help you today?")
    while True:
        user_input = input("> ").lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        response = get_response(user_input)
        print(response)

if __name__ == '__main__':
    main()

#Limitations include:
# Limited functionalitity - Did not use libraries
# Scaling difficuliess
# Longer development time - Without pre-existing libraries