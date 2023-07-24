import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Download the 'punkt' tokenizer (only needs to be done once)
nltk.download('punkt')

# Define the chatbot responses
pairs = [
    [
        r"hello|hi|hey",
        ["Hello!", "Hi!", "Hey!"]
    ],
    # Add more chatbot responses here
    [
        r"How many departments are there in this university?",
        ["6 departments"]
    ],
    # ...
    [
        r"quit|exit",
        ["Bye! It was nice talking to you.", "Goodbye! Have a great day!"]
    ]
]


# Create the chatbot

def simple_chatbot():
    # st.title("Simple Chatbot")
    st.markdown("<h1 style='text-align: center; color: orange;'>University Query Chatbot</h1>", unsafe_allow_html=True)
    st.write("Hello! I'm a simple chatbot. You can type 'quit' to exit.")
    chatbot = Chat(pairs, reflections)

    counter = 0
    user_input = st.text_input("You: ", key=counter)
    if st.button("Enter"):
        if user_input.lower() in ["quit", "exit"]:
            st.write("Chatbot: Goodbye! It was nice talking to you.")
        else:
            response = chatbot.respond(user_input)
            st.write("Chatbot:", response)


if __name__ == "__main__":
    simple_chatbot()
