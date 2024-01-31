# model: gpt-3.5-turbo-instruct
# from openai import OpenAI
# client = OpenAI()
# message
from dotenv import load_dotenv
from sendmesssage import send_message

import streamlit as st
from streamlit_chat import message

load_dotenv()

st.title("Sayvai Software LLP welcomes you")
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = []
 
if 'openai_response' not in st.session_state:
    st.session_state['openai_response'] = []
 
def get_text():
    input_text = st.text_input("Lets talk", key="input")
    return input_text
 
user_input = get_text()
 
if user_input:
    output = send_message(user_input)
    output = output.lstrip("\n")
 
    # Store the output
    st.session_state.openai_response.append(user_input)
    st.session_state.user_input.append(output)
 
message_history = st.empty()
 
if st.session_state['user_input']:
    for i in range(len(st.session_state['user_input']) - 1, -1, -1):
        # This function displays user input
        message(st.session_state["user_input"][i], 
                key=str(i),avatar_style="icons")
        # This function displays OpenAI response
        message(st.session_state['openai_response'][i], 
                avatar_style="miniavs",is_user=True,
                key=str(i) + 'data_by_user')