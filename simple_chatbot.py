import nltk
from nltk.chat.util import Chat, reflections


# Define the chatbot responses
pairs = [
    [
        r"hello|hi|hey",
        ["Hello!", "Hi!", "Hey!", ]
    ],
    [
        r"what is your name?",
        ["I am a chatbot.", "I'm a chatbot.", "Call me Chatbot."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm fine, thanks!"]
    ],
    [
        r"what is your favorite color?",
        ["I don't have favorite colors as I am a chatbot.", "I'm just a program, I don't have preferences."]
    ],
    [
        r"quit|exit",
        ["Bye! It was nice talking to you.", "Goodbye! Have a great day!"]
    ]
]


# Create the chatbot
def simplechatbot():
    print("Hello! I'm a simple chatbot. You can type 'quit' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()


if __name__ == "__main__":
    # nltk.download('punkt')
    simplechatbot()
