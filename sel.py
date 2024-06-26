import streamlit as st

from ATS import run as ats_run
from main_classes import run as main_classes_run

# Navigation options
nav_options = ["Job Description", "ATS (Applicant Tracking System)", "Management"]

# Create the fixed navbar using Streamlit components
st.sidebar.title("Navigation")
selected_parameter = st.sidebar.selectbox("Select Parameter:", nav_options)

# Display content based on selected parameter (replace with your actual content)
if selected_parameter == "Job Description":
    st.write("Job Description Content in development")
    
elif selected_parameter == "ATS (Applicant Tracking System)":
    st.write("ATS Information")
    ats_run()
elif selected_parameter == "Management":
    st.write("Management Skills Evaluation in development")
    main_classes_run()
else:
    st.write("Please select a parameter from the sidebar.")


