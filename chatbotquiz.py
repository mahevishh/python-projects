import streamlit as st
from nltk.chat.util import Chat, reflections

# Chatbot patterns & responses
pairs = [
    [r"my name is (.*)", ["Hello %1, nice to meet you!", "Hi %1! How are you today?"]],
    [r"i am good|i am fine|it's good|it's nice", ["glad"]],
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi, how can I help you today?"]],
    [r"how are you ?", ["I'm doing well, thank you!", "I'm fine, how about you?"]],
    [r"what is your name ?", ["I'm ChatBot created with NLTK.", "You can call me ChatBot!"]],
    [r"where are you from ?", ["I'm from the world of Python and NLTK!"]],
    [r"(.*) weather (.*)", ["I'm not sure, but you can check a weather website for that."]],
    [r"quit", ["Goodbye! Have a nice day.", "Bye! It was nice talking to you."]],
    [r"(.*)", ["I'm sorry, I don't understand that.", "Can you rephrase?"]]
]

# Create Chatbot
chat = Chat(pairs, reflections)

# --- Streamlit UI ---
st.set_page_config(page_title="ChatBot", page_icon="🤖", layout="centered")
st.title("🤖 NLTK ChatBot")

# Minimal CSS for cleaner chat bubbles
st.markdown("""
<style>
.chat-container {
    max-height: 400px;
    overflow-y: auto;
    padding: 10px;
    background-color: #f9f9f9;
    border-radius: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
}
.user-bubble, .bot-bubble {
    padding: 6px 10px;
    border-radius: 8px;
    margin: 4px 0;
    display: inline-block;
}
.user-bubble {
    background-color: #e0e0e0;
    text-align: right;
}
.bot-bubble {
    background-color: #ffffff;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for role, message in st.session_state.chat_history:
    if role == "You":
        st.markdown(f'<div class="user-bubble">{message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">{message}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Input area at the bottom
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", "")
    send = st.form_submit_button("Send")

# When user submits message
if send and user_input:
    response = chat.respond(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))
    st.rerun()  # ✅ works in latest Streamlit
