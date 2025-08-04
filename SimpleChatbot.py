import streamlit as st
import google.generativeai as genai

# Configure Streamlit page
st.set_page_config(page_title="Minimal Gemini Chatbot", page_icon=":robot_face:")

# Application Title
st.title("Minimal Gemini Chatbot")
st.write("This is a bare-bones example of a Streamlit chatbot using Google Gemini 1.5 Flash.")
st.write("Please enter your Gemini API Key in the sidebar to start chatting.")

# API Key Input in sidebar
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.markdown("---") # Separator for clarity

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Only proceed if API key is provided
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Accept user input
    if prompt := st.chat_input("What would you like to ask?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get Gemini response
        with st.chat_message("assistant"):
            chat = model.start_chat(history=[])
            response = chat.send_message(prompt)
            full_response = response.text
            st.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})
else:
    st.info("Please enter your Gemini API Key in the sidebar to start chatting.")
