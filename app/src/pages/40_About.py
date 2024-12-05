import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    Are you a student who wants to be able to easily find a co-op? 🧑‍🎓
    
    Are you a recruiter that requires a way to sort through all of the students based on needed metrics? 🤔
    
    Are you a school that needs to implement a solution for your co-op program with efficiency and simplicity? 🏫
    
    Look no further than COSINT! An application designed for your co-op needs😁

    Please give feedback as we are always developing new features! 🚀
    """
        )
