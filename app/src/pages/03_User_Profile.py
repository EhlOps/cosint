import logging
logger = logging.getLogger(__name__)

import streamlit as st
import requests
import pandas as pd
import numpy as np
from modules.nav import SideBarLinks
from datetime import date

st.set_page_config(layout = 'wide')

SideBarLinks()

try:
    response = requests.get(
        f"http://api:4000/users/{st.session_state['profile_id']}"
    )
    if response.status_code == 200:
        data = response.json()[0]
        st.title(f"{data['name']}'s Profile")
        st.image(data['profilePic'], width=150)
        st.write("Pronouns:")
        st.write(str(data['pronouns']))
        st.write("Preferred Name:")
        st.write(str(data['preferredName']))
        st.write("Age:",)
        st.write(str(int(date.today().year) - int(data['birthday'].year) - ((date.today().month, date.today().day) < (data['birthday'].month, data['birthday'].day))))
        st.write("Email:",)
        st.write(str(data['email']))
        st.write("Phone Number:",)
        st.write(str(data['mobile']))
        st.write("Last Active:")
        if(data[active]):
            st.write(str(now))
        else:
            (data['lastLogin'])
        st.write("Bio:",)
        st.write(data['profile'])
except requests.exceptions.RequestException as e:
    st.error(f"Error connecting to server: {str(e)}")

if st.session_state["id"] == st.session_state["profile_id"]:
    if st.button('Edit Profile', 
             type='primary',
             use_container_width=True):
      st.switch_page('pages/04_User_Profile_Editor.py')