import spacy
print(spacy.__version__)

nlp=spacy.load("en_core_web_sm")


intents = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you"],
    "thanks": ["thank you", "thanks", "thx"],
    "name": ["your name", "who are you"],
    "weather": ["weather", "climate", "temperature"]
}

responses = {
    "greeting": "Hello! How can I help you?",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "name": "I am a simple chatbot created using spaCy.",
    "weather": "I'm not connected to the internet, but I hope it's sunny!"
}



def get_intent(text):
    doc = nlp(text.lower())
    for token in doc:
        for intent, keywords in intents.items():
            if token.text in keywords:
                return intent
    return "unknown"



print("Bot: Hi! I’m your chatbot. Ask me anything (type 'exit' to quit).")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Bye! 👋")
        break

    intent = get_intent(user_input)
    response = responses.get(intent, "I'm not sure how to respond to that.")
    print("Bot:", response)
