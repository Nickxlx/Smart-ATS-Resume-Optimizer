import os
from dotenv import load_dotenv
import PyPDF2 as pdf
import streamlit as st
from langchain.llms import Cohere

# Load environment variables
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not COHERE_API_KEY:
    st.error("❌ COHERE API key not found. Please check your .env file.")
    st.stop()

# Initialize Cohere model
model = Cohere(
    cohere_api_key=COHERE_API_KEY,
    temperature=0,
    max_tokens=1000,
    model="command-r-plus"
)

# Upload PDF resume
def uploaded_pdf_to_text(uploaded_file):
    try:
        if not uploaded_file.name.endswith('.pdf'):
            st.error("❌ Please upload a valid PDF file.")
            return ""
        
        # Read the PDF file
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
    except Exception as e:
        st.error(f"❌ Error reading PDF: {e}")
        return ""

# Generate response
def get_ai_response(input_prompt, resume_txt, jd):
    try:
        prompt = f"{input_prompt}\n\nResume:\n{resume_txt}\n\nJob Description:\n{jd}"
        response = model.invoke(prompt)
        return response
    except Exception as e:
        return str(e)

# Streamlit UI - Enhanced Header & Instructions
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color: #1f77b4; margin-bottom: 0;'>🚀 Smart ATS: Resume Optimizer</h1>
        <h3 style='color: #cb4335; margin-top: 0;'>Make Your Resume Stand Out for Any Job!</h3>
    </div>
    """,
    unsafe_allow_html=True
)

job_description = st.text_area("", help="Copy and paste the job description here", placeholder="Paste job description here...", label_visibility="hidden")
uploaded_file = st.file_uploader("", type="pdf", help="Please upload your resume in PDF format", label_visibility="hidden")

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

# Improved prompt templates
input_prompt1 = """
You are an advanced Applicant Tracking System (ATS) evaluator.
Carefully compare the candidate's resume with the provided job description.
Analyze skills, experience, education, and relevant keywords.
Calculate the overall percentage match between the resume and the job description.
Respond ONLY in this format: Job Description Match: "XX%".
Do not include any explanation or extra text.
"""

input_prompt2 = """
You are an ATS optimization expert.
Thoroughly review the job description and the candidate's resume.
Identify ONLY the most critical missing skills, qualifications, or keywords from the job description that would significantly impact the candidate's chances of being selected.
List ONLY these highly important missing keywords or skills as bullet points in this format:
Missing Critical Keywords:
- keyword 1
- keyword 2
Do not include any explanation or extra text.
"""

input_prompt3 = """
You are an AI specializing in ATS resume analysis.
Compare the resume and job description in detail.
Provide the following in your response:
Job Description Match: "XX%" (percentage match based on skills, experience, and keywords)
Missing Critical Keywords: (bullet list of the most important keywords or skills from the job description that are missing from the resume and could strongly affect selection chances)
Profile Summary: (a concise, candidate-focused summary explaining how well the resume aligns with the job description, highlighting key gaps, and providing actionable suggestions for improving alignment and increasing the chances of being shortlisted)
Format your response exactly as shown above, with no extra commentary.
"""

def process_resume(prompt_template):
    if uploaded_file and job_description:
        resume_text = uploaded_pdf_to_text(uploaded_file)
        with st.spinner("🔄 Analyzing..."):
            return get_ai_response(prompt_template, resume_text, job_description)
    else:
        st.warning("⚠️ Please upload your resume and paste the job description.")
        return None
    
## Trigger analysis
if submit1:
    result = process_resume(input_prompt1)
    if result:
        st.subheader("📈 Percentage Match")
        st.write(result, language="markdown")

elif submit2:
    result = process_resume(input_prompt2)
    if result:
        st.subheader("⚠️ Missing Skills")
        st.write(result, language="markdown")

elif submit3:
    result = process_resume(input_prompt3)
    if result:
        st.subheader("📊 Detailed Resume Analysis")
        st.write(result)