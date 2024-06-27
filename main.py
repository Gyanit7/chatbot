import nltk
import random
import string
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.chat.util import Chat, reflections


nltk.download('punkt')
nltk.download('wordnet')


lemmatizer = WordNetLemmatizer()

def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in string.punctuation]
    return lemmatized_tokens


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"(hi|hello|hey|hola|howdy)",
        ["Hello!", "Hi there!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"i am (.*) (good|well|okay|ok)",
        ["Nice to hear that!", "How can I assist you today?",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created to assist you.",]
    ],
    [
        r"who created you ?",
        ["I was created using Python and the NLTK library.",]
    ],
    [
        r"what can you do ?",
        ["I can help you with basic queries, chat with you, and provide information.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am a virtual entity, but I can assist you from anywhere.",]
    ],
    [
        r"how is the weather in (.*)",
        ["I don't have access to real-time weather data. You can check a weather website.",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a chatbot, but I can help you find information about sports or games.",]
    ],
    [
        r"(bye|exit|quit)",
        ["Goodbye! It was nice talking to you.", "Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Could you please rephrase?", "Can you clarify that for me?"]
    ]
]


reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}


chatbot = Chat(pairs, reflections)


def start_chatbot():
    print("Hi! I'm an advanced chatbot. How can I assist you today? (type 'quit' to exit)")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you please rephrase?")


start_chatbot()
