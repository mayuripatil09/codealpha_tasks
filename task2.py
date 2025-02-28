import nltk
import spacy
import random
import pyttsx3
from textblob import TextBlob
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext, messagebox

nlp = spacy.load("en_core_web_sm")
engine = pyttsx3.init()

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! Nice to meet you. How can I assist you today?"]
    ],
    [
        r"what is your name?",
        ["I'm ChatBot, your friendly AI assistant. You can call me CB for short!"]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thanks for asking! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No worries, %1! We all make mistakes.", "It's alright, don't stress about it."]
    ],
    [
        r"quit",
        ["Goodbye! It was nice chatting with you. See you soon!"]
    ],
    [
        r"(.*) (age|old) ?",
        ["I'm just a program, so I don't have an age. But I'm always learning!"]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to help you with whatever you need. Just ask!"]
    ],
    [
        r"(.*) created you ?",
        ["I was created by a talented developer using Python and NLP libraries."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I exist in the digital world, so I don't have a physical location. But I'm always here for you!"]
    ],
    [
        r"how (.) health (.)",
        ["I'm a chatbot, so I don't have health, but I appreciate your concern!"]
    ],
    [
        r"(.) (weather|temperature) (.)",
        ["I'm not connected to the internet, so I can't provide real-time weather information. But you can check your favorite weather app!"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"thank you",
        ["You're welcome!", "No problem, happy to help!", "Anytime!"]
    ],
    [
        r"(.) (love|like) (.)",
        ["That's awesome! I'm glad you like %3.", "I love %3 too! It's one of my favorites."]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, tell jokes, answer questions, and even help you learn new things!"]
    ],
    [
        r"(.) (music|song) (.)",
        ["I don't have ears, but I love the idea of music! What's your favorite song?"]
    ],
    [
        r"(.) (food|eat) (.)",
        ["I can't eat, but I hear %3 is delicious! What's your favorite food?"]
    ],
    [
        r"(.*)",
        ["Hmm, I'm not sure I understand. Can you rephrase that?", "Interesting! Tell me more."]
    ]
]

chatbot = Chat(pairs, reflections)

user_info = {
    "name": None,
    "favorite_food": None,
    "favorite_music": None,
}

def process_text_with_spacy(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    sentiment = TextBlob(text).sentiment.polarity
    sentiment_label = "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral"
    return entities, sentiment_label

def get_fallback_response(user_input):
    fallback_responses = [
        "That's interesting! Can you tell me more?",
        "I'm still learning. Could you explain that in another way?",
        "I'm not sure I understand. Let's talk about something else!",
        "Hmm, I don't know much about that. What else are you interested in?",
    ]
    return random.choice(fallback_responses)

def handle_user_input():
    user_input = user_entry.get()
    if user_input.lower() == "quit":
        chat_window.insert(tk.END, "ChatBot: Goodbye! It was nice chatting with you. See you soon!\n")
        engine.say("Goodbye! It was nice chatting with you. See you soon!")
        engine.runAndWait()
        root.quit()
    else:
        chat_window.insert(tk.END, f"You: {user_input}\n")
        entities, sentiment = process_text_with_spacy(user_input)
        if entities:
            chat_window.insert(tk.END, f"ChatBot: I detected the following entities: {entities}\n")
        chat_window.insert(tk.END, f"ChatBot: You seem to be in a {sentiment} mood.\n")

        for entity, label in entities:
            if label == "PERSON" and not user_info["name"]:
                user_info["name"] = entity
                chat_window.insert(tk.END, f"ChatBot: Nice to meet you, {user_info['name']}!\n")
            elif label == "FOOD" and not user_info["favorite_food"]:
                user_info["favorite_food"] = entity
                chat_window.insert(tk.END, f"ChatBot: I see you like {user_info['favorite_food']}. Yum!\n")
            elif label == "MUSIC" and not user_info["favorite_music"]:
                user_info["favorite_music"] = entity
                chat_window.insert(tk.END, f"ChatBot: {user_info['favorite_music']} is a great choice!\n")

        response = chatbot.respond(user_input)
        if response:
            chat_window.insert(tk.END, f"ChatBot: {response}\n")
            engine.say(response)
            engine.runAndWait()
        else:
            fallback_response = get_fallback_response(user_input)
            chat_window.insert(tk.END, f"ChatBot: {fallback_response}\n")
            engine.say(fallback_response)
            engine.runAndWait()

        user_entry.delete(0, tk.END)

def show_info():
    messagebox.showinfo("About ChatBot", "ChatBot v1.0\nDeveloped using Python and NLP libraries.\nEnjoy chatting!")

root = tk.Tk()
root.title("Advanced ChatBot")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="#2c3e50")

chat_frame = tk.Frame(root, bg="#34495e", bd=5)
chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_window = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=60, height=20, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.insert(tk.END, "ChatBot: Hi! I'm ChatBot, your friendly AI assistant. Type 'quit' to exit.\n")

user_entry = tk.Entry(root, width=50, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50")
user_entry.pack(padx=10, pady=10, fill=tk.X)
user_entry.bind("<Return>", lambda event: handle_user_input())

button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(padx=10, pady=10, fill=tk.X)

send_button = tk.Button(button_frame, text="Send", command=handle_user_input, font=("Arial", 14), bg="#3498db", fg="#ecf0f1", bd=0)
send_button.pack(side=tk.LEFT, padx=5, pady=5)

info_button = tk.Button(button_frame, text="Info", command=show_info, font=("Arial", 14), bg="#e74c3c", fg="#ecf0f1", bd=0)
info_button.pack(side=tk.RIGHT, padx=5, pady=5)

root.mainloop()
