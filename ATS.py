from docx import Document
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st


def run():
    st.write("ATS running now")

    def convert(file_object):  # Accept a file object for flexibility
        document = Document(file_object)
        text = ""
        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"
        return text

    job_file = st.file_uploader("Choose a job description to upload", type="docx")  # Specify file type
    resume_file = st.file_uploader("Choose a resume to upload", type="docx")

    if job_file is not None and resume_file is not None:
        try:
            job_desc = convert(job_file)  # Apply convert function with file object
            resume = convert(resume_file)

            text = [resume, job_desc]  # Ensure order for similarity comparison
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(text)

            match = cosine_similarity(count_matrix)[0][1]  # Access similarity score
            match = round(match * 100, 2)

            st.write("This resume has a score of", match, "%")
        except Exception as e:
            st.error("An error occurred:", e)
    else:
        st.info("Upload both a job description and a resume to proceed.")


