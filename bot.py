import streamlit as st
from gemini import conversation
from datetime import datetime
from time import sleep

st.title("Welcome Sir !")

def initialize_chat_history():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "store_msg" not in st.session_state:
        st.session_state.store_msg = []

def display_chat_history():
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def display_output(role, content):
    # Display output message
    role = role.lower()
    with st.chat_message(role):
        st.markdown(content)
    # Add message to session state
    st.session_state.messages.append({"role": role, "content": content})

def process_user_input(full_prompt, prompt):
    # Process user input
    if prompt:
        # Display user input
        display_output('user', prompt)
        # Generate assistant reply
        reply = conversation(full_prompt)
        if not reply == 'Sorry can not process your input':
            # Display assistant reply
            display_output('assistant', reply)
        else:
            response = f"Audy : {reply}"
            display_output('assistant', response)

def date_time():
    # Get current date and time
    current_datetime = datetime.now()
    # Format date and time
    formatted_datetime = current_datetime.strftime("%A, %Y-%m-%d %H:%M:%S")
    return formatted_datetime

def main(filtered_contact):
    '''
    Returns prompt from project manager
    '''
    
    # Initialize chat history
    initialize_chat_history()
    # Display chat history
    display_chat_history()

    # Choose relation
    options = ["Message for co-worker...", "Message for family member...", "Message for friend..."]
    relation = st.selectbox("Choose any one Relation", options)

    # Filter names based on selected relation
    if relation == "Message for co-worker...":
        names = filtered_contact[filtered_contact['Relationship Status'].str.contains('coworker', case=False)]['Name']
    elif relation == "Message for family member...":
        names = filtered_contact[filtered_contact['Relationship Status'].str.contains('family', case=False)]['Name']
    elif relation == "Message for friend...":
        names = filtered_contact[filtered_contact['Relationship Status'].str.contains('friend', case=False)]['Name']

    # Select person to message
    selected_person = st.selectbox("Select the person to whom you want to send a message.", names, key="1")
    time = date_time()

    # Construct initial prompt
    inbuilt_prompt = f'''You are a motivator, friend and project manager of {selected_person}. After identifying the gender of the person -
    dont put all questions at once. converse like a human, keep track of old conversation.
    Greet {selected_person}, it's {time} . Ask him is he well?
    Ask him / her about what was the assignment given to them ? , when it was given ? , what is the latest update of the task? , What did he understood about the task and all. No need to go into very conversational mode, just be simple and straightdorward. Analyze from past conversations , what all questions you have already asked and what remains. \n
    '''

    # Input message
    prompt = st.text_area(f"Type message for {selected_person}")

    # Button to add message
    
    msg_button,del_button=st.columns(2)
    with  msg_button:
        add_msg_button = st.button("Add Message")
    
        if add_msg_button :
            if not prompt:
                st.error('Please type your message first', icon="🚨")
            elif "store_msg" in st.session_state:
                # Add message to session state
                st.session_state.store_msg.append(prompt)
                st.success(f'''Processing successfull. Just a second''')
                # Delay and rerun to update UI
                sleep(3)
                st.experimental_rerun()
        
    with del_button:
        # add_del_button = st.button("Delete message", key=f"delete_button")
        if st.button("Delete all message"):
            st.session_state.store_msg.clear()
            st.success("All messages deleted!")
            st.experimental_rerun()



    # Arrange messages in two columns
    col1, col2 = st.columns(2)
    store_msg = st.session_state.store_msg
    for i in range(len(store_msg)):
        if i % 2 == 0:
            with col1:
                if st.button(store_msg[i], key=f"Button_{i}"):  # Unique key for each button
                    # Display success message and delay before rerun
                    prompt = store_msg[i]
                    st.success(f'''Processing successfull Just a second''')
                    sleep(3)
                    st.experimental_rerun()
        else:
            with col2:
                if st.button(store_msg[i], key=f"Button_{i}"):  # Unique key for each button
                    # Display success message and delay before rerun
                    prompt = store_msg[i]
                    st.success(f'''Processing successfull. Just a second''')
                    sleep(3)
                    st.experimental_rerun()

    # Combine prompts
    full_prompt = str(inbuilt_prompt) + str(prompt)
    

    if st.button("Send"):
        return prompt

                
