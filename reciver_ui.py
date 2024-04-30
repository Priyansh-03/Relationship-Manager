# reciver_ui.py
import streamlit as st

def main():
    st.title("Receiver Interface")
    if 'messages' not in st.session_state:
        st.session_state.messages = ["Welcome to the Receiver Interface!"]
    
    for message in st.session_state.messages:
        st.write(message)
    
    user_input = st.text_input("Type your response")
    if st.button("Send"):
        st.session_state.messages.append(user_input)

if __name__ == "__main__":
    main()
