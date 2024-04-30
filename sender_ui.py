import streamlit as st
from streamlit_option_menu import option_menu
import pickle as pk
import bot
import reciver_ui
import threading
import subprocess

# Load data
with open("filtered_contact.pkl", "rb") as file:
    filtered_contact = pk.load(file)




# Assume 'Name' is a column where each entry is a string of names separated by commas
# Apply .str accessor to split names and then explode to make each name a separate row if necessary.
# If each cell contains multiple names separated by commas:
if 'Name' in filtered_contact.columns:
    names = filtered_contact['Name'].str.split(',').explode().str.strip().dropna().unique()
    names.sort()


def sidebar():
    
    with st.sidebar:
        
        # Primary menu selection
        selected = option_menu(
            menu_title='Chats',
            options=['BOT', 'USERS'],  # Users will trigger the display of the submenu-like list
            menu_icon='chat-text-fill',
            default_index=0,
            
            # Altername Styles provided

            # styles={
            #     "container": {"padding": "5!important", "background-color": 'black'},
            #     "icon": {"color": "orange", "font-size": "25px"},
            #     "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "color": "white"},
            #     "nav-link-selected": {"background-color": "#02ab21"}
            # }

            styles={"container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "17px"},
                    "nav-link": {"color": "white", "font-size": "15px", "text-align": "left", "margin": "0px"},
                    "nav-link-selector": {"background-color": "#02ab21"}}
        )

        # If 'USERS' is selected, display a secondary selectable list of names
        if selected == 'USERS':
            # user_selected = st.selectbox('Select a User', names)
            user_selected = st.selectbox('Select a User', names)
            return 'USERS', user_selected
        return selected, None



def run_receiver_ui():
    """Function to run the receiver UI in a separate thread."""
    # This command runs the streamlit app
    subprocess.run(["streamlit", "run", "reciver_ui.py"])



def app():
    selected_option, user_selected = sidebar()  # Call the sidebar function to handle menu options
    
    if selected_option == 'USERS' and user_selected:
        st.write(f'You have selected user: {user_selected}')
    else:
        prompt=bot.main(filtered_contact)
        run_receiver_ui()
        receiver_thread = threading.Thread(target=run_receiver_ui)
        receiver_thread.start()
        
    

app()
