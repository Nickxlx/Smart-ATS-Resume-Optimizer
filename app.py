import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Handel input pdf
def uploaded_pdf_to_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        page_text = str(page.extract_text)
        if page_text:
            text+=page_text + "\n"

    return text.strip()

# generate response using gemini-pro
def get_genai_response(input_prompt, pdf_text, jd):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content([input_prompt, pdf_text[0], jd])
        return response
    except Exception as e:
        return str(e)

# Streamlit App Layout and Style
st.markdown("<h2 style='text-align: center; color: #1f77b4;'>Smart ATS: Resume Optimization Tool</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #cb4335 ;'>Enhance your resume for ATS compatibility</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Boost your chances of getting selected by matching your resume with the job description.</p>", unsafe_allow_html=True)

st.markdown("#### Paste the Job Description")
jd=st.text_area("Paste the Job Description", help="Copy and paste the job description here", label_visibility = "hidden")
st.markdown("#### Uplode you Resume (PDF) ")
uploaded_file=st.file_uploader("Upload Your Resume(PDF)", type="pdf", help="Please upload your resume in PDF format",label_visibility="hidden")

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Button Actions
st.markdown("### Select an Option:")
col1, col2, col3 = st.columns(3)
with col1:
    submit1 = st.button("🔍 Percentage Match")
with col2:
    submit2 = st.button("⚙️ Missing Skills")
with col3:
    submit3 = st.button("📊 Detailed Analysis")

# detaild prompt Template
input_prompt1 = """
You are an ATS (Applicant Tracking System) scanner.
Evaluate the resume against the job description provided and calculate the percentage match between the two.
Respond in this format: Job Description Match: "XX%". Ensure a precise and fair match.
"""


input_prompt2 = """
You are an ATS (Applicant Tracking System) scanner. 
Identify the missing skills or keywords from the job description that are absent in the resume.
Respond in this format: Missing Keywords: [list of missing keywords in points].
"""

input_prompt3 = """
You are an advanced AI specialized in analyzing resumes and job descriptions for Applicant Tracking Systems (ATS). 

Your task is to evaluate the provided resume text against the given job description for a data science or technical role. The analysis must be highly accurate and comprehensive, considering relevant keywords, skills, experiences, and qualifications.

**Instructions:**
1. Calculate the percentage match between the job description and the resume based on relevant keywords, skills, and required qualifications. 
2. Identify any missing or under-represented skills and keywords in the resume that are present in the job description.
3. Provide a concise profile summary based on the resume text, including the main skills and experiences of the candidate.

Respond in this format:

Job Description Match: "XX%",\n

Missing Keywords: [list of missing keywords in points],\n

Profile Summary: "Brief summary of the profile."
}"""
if submit1: 
    if uploaded_file is not None:
        text = uploaded_pdf_to_text(uploaded_file)
        response = get_genai_response(input_prompt1, text, jd)
        st.subheader("Percentage Match Result")
        st.write(response.text)
    else:
        st.write("Please uplaod the resume")
elif submit2: 
    if uploaded_file is not None:
        text = uploaded_pdf_to_text(uploaded_file)
        response = get_genai_response(input_prompt2, text, jd)
        st.subheader("Missing Skills Result")
        st.write(response.text)
    else:
        st.write("Please uplaod the resume")

elif submit3: 
    if uploaded_file is not None:
        pdf_text = uploaded_pdf_to_text(uploaded_file)
        response = get_genai_response(input_prompt3, pdf_text, jd)
        st.subheader("Detailed Resume Analysis")
        st.write(response.text)
    else:
        st.write("Please uplaod the resume")
