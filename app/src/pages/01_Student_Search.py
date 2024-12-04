import logging

logger = logging.getLogger(__name__)

import streamlit as st
import requests
import pandas as pd
import numpy as np
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

SideBarLinks()

st.title(f"Student Search")

try:
    test_response = requests.get("http://api:4000/stu/students")

    if not test_response.status_code == 200:
        st.error("Failed to fetch categories")
except requests.exceptions.RequestException as e:
    st.error(f"Error connecting to students API: {str(e)}")

with st.form("student_search"):
    student_value = student_input = st.text_input(
        "Search Students",
        placeholder="Enter student name or Id#",
    )

    #    if st.session_state["role"] == "employer":
    #        student_type = st.radio(
    #            "Student Type",
    #            options=["All", "Applied", "Flagged",],
    #        )

    submit_button = st.form_submit_button("Search")

    if submit_button:
        if not student_value:
            st.error("Please enter a student name or id")
        else:
            logger.info(f"Student form submitted with data: {student_value}")

            try:
                response = requests.get(
                    f"http://api:4000/stu/students/search/{student_value}"
                )
                if response.status_code == 200:
                    st.success(f"{response.json()}")
                else:
                    st.error(f"Error adding accessing api: {response.status_code}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
