import os
from dotenv import load_dotenv
import streamlit as st
import PyPDF2 as pdf
from langchain.llms import Cohere

# Load API key
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# ✅ Initialize model
model = Cohere(
    temperature=0,
    max_tokens=1000,
    model="command-r-plus",)

# Handle uploaded PDF resume
def uploaded_pdf_to_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

# Generate response
def get_ai_response(input_prompt, resume_txt, jd):
    try:
        prompt = f"{input_prompt}\n\nResume:\n{resume_txt}\n\nJob Description:\n{jd}"
        response = model.invoke(prompt)
        return response
    except Exception as e:
        return str(e)

# Streamlit UI
st.markdown("<h2 style='text-align: center; color: #1f77b4;'>Smart ATS: Resume Optimization Tool</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #cb4335;'>Enhance your resume for ATS compatibility</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Boost your chances of getting selected by matching your resume with the job description.</p>", unsafe_allow_html=True)

job_description = st.text_area("Paste the Job Description", help="Copy and paste the job description here", label_visibility="hidden")
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf", help="Please upload your resume in PDF format", label_visibility="hidden")

if uploaded_file is not None:
    st.success("✅ PDF Uploaded Successfully!")

# Button UI
col1, col2, col3 = st.columns(3)
with col1:
    submit1 = st.button("🔍 Percentage Match")
with col2:
    submit2 = st.button("⚙️ Missing Skills")
with col3:
    submit3 = st.button("📊 Detailed Analysis")

# Prompt templates
input_prompt1 = """
You are an ATS (Applicant Tracking System) scanner.
Evaluate the resume against the job description provided and calculate the percentage match between both of them.
Your response should be only in this format: Job Description Match: "XX%".
"""

input_prompt2 = """
You are an ATS scanner. Identify the missing skills or keywords from the job description that are absent in the resume.
Respond in this format: Missing Keywords: [list of missing keywords in points].
"""

input_prompt3 = """
You are an AI specializing in ATS resume matching. 
Evaluate the provided resume against the job description and respond in this format:

Job Description Match: "XX%"
Missing Keywords: [list of missing keywords in points]
Profile Summary: "Brief summary of the profile."
"""

# Trigger actions
if submit1:
    if uploaded_file and job_description:
        text = uploaded_pdf_to_text(uploaded_file)
        response = get_ai_response(input_prompt1, text, job_description)
        st.subheader("📈 Percentage Match")
        st.write(response)
    else:
        st.warning("⚠️ Please upload your resume and paste the job description.")

elif submit2:
    if uploaded_file and job_description:
        text = uploaded_pdf_to_text(uploaded_file)
        response = get_ai_response(input_prompt2, text, job_description)
        st.subheader("⚠️ Missing Skills")
        st.write(response)
    else:
        st.warning("⚠️ Please upload your resume and paste the job description.")

elif submit3:
    if uploaded_file and job_description:
        text = uploaded_pdf_to_text(uploaded_file)
        response = get_ai_response(input_prompt3, text, job_description)
        st.subheader("📊 Detailed Resume Analysis")
        st.write(response)
    else:
        st.warning("⚠️ Please upload your resume and paste the job description.")
