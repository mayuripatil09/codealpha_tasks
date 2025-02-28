# codealpha_tasks
#task1-Hangmangame
Word Guessing Game

Introduction

This is a simple word guessing game implemented in Python. The game selects a random word from a predefined list, and the player has to guess the word by guessing one letter at a time. The player has a limited number of chances to guess the correct word.

Features

Random word selection

Limited number of attempts (7 chances)

Displays progress after each guess

Checks for correct and incorrect letters

Congratulates the player upon winning

Reveals the correct word if the player loses


How to Play

1. The game will display a hidden word using dashes (-), where each dash represents a letter.


2. The player inputs a letter to guess.


3. If the letter is in the word, it is revealed in its correct position.


4. If the letter is incorrect, the player loses one chance.


5. The game continues until the player either guesses the word correctly or runs out of chances.



Example

-----
Guess a letter: A  
A--A-  
Guess a letter: P  
AP-A-  
Guess a letter: L  
APPL-  
Guess a letter: E  
APPLE  
Congratulations! You won!!

Installation and Execution

To run the game, follow these steps:

1. Clone the repository:

git clone https://github.com/yourusername/word_guessing_game.git
cd word_guessing_game


2. Run the script:

python word_guessing_game.py



Contribution

Feel free to contribute by adding more words, improving the game logic, or enhancing the user experience. Fork the repository and submit a pull request with your changes.

License

This project is licensed under the MIT License. See the LICENSE file for more details.


#task-2:Basic ChatBot
Basic ChatBot

Introduction

Welcome to the Advanced ChatBot! This chatbot is developed using Python and Natural Language Processing (NLP) libraries. It can chat with you, tell jokes, answer questions, and even help you learn new things. The chatbot comes with a user-friendly GUI and text-to-speech capabilities.

Features

Chat with the bot

Get jokes and fun replies

Text-to-speech responses

Information about the chatbot

User-friendly GUI


Installation

To run this chatbot, you need to have Python installed along with a few libraries. Follow the steps below to set up the environment:

1. Clone the repository:

git clone https://github.com/yourusername/advanced_chatbot.git
cd advanced_chatbot


2. Install required libraries:

pip install nltk spacy requests textblob pyttsx3
python -m spacy download en_core_web_sm
python -m textblob.download_corpora


3. Run the chatbot:

python advanced_chatbot_gui.py



How to Use

1. Start the chatbot: Run the script advanced_chatbot_gui.py to launch the chatbot GUI.


2. Chat with the bot: Type your messages in the input field and press "Send" or hit Enter.


3. Get information: Press the "Info" button to get information about the chatbot.


4. End the chat: Type "quit" to end the chat session.



Example Questions

Here are some example questions you can ask the chatbot:

What's your name?

How are you?

Tell me a joke.

What's the weather like?

Who created you?

What can you do?


Contribution

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes. We welcome all contributions that improve the functionality and user experience of the chatbot.

License

This project is licensed under the MIT License. See the LICENSE file for more details.
