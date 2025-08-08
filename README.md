# Smart ATS: Resume Optimization Tool

## 🚀 Project Overview

The **Smart ATS: Resume Optimization Tool** is an interactive application designed to enhance resumes for Applicant Tracking Systems (ATS). This tool analyzes a resume against a job description (JD), providing insights into how well the resume matches the job requirements. The analysis is powered by **Cohere's language model** to ensure precise and actionable results.

## ✅ Features

- **🔍 Percentage Match**: Calculates how well the resume matches the job description.
- **⚙️ Missing Skills**: Identifies key skills or keywords from the JD that are not present in the resume.
- **📊 Detailed Analysis**: Offers a comprehensive analysis including percentage match, missing skills, and a brief profile summary.

## 🛠️ Tech Stack

- **Streamlit** – For creating the user-friendly web interface.
- **Cohere LLM** – For performing AI-based text evaluation.
- **LangChain** – To integrate LLM calls.
- **PyPDF2** – To extract text from uploaded PDF resumes.
- **dotenv** – For securely loading API keys and environment variables.

## 🧠 How It Works

1. **Upload Resume** – Upload your resume in PDF format.
2. **Paste Job Description** – Copy and paste the JD into the input field.
3. **Select Analysis Type**:
   - **Percentage Match** – Get a match score between resume and JD.
   - **Missing Skills** – See what essential skills are missing.
   - **Detailed Analysis** – Get all of the above plus a profile summary.

## ⚙️ Setup Instructions

### ✅ Prerequisites

Ensure the following are installed:

- Python 3.9 or 3.10
- pip or conda
- Cohere API key (get from https://cohere.com)

### 📦 Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Nickxlx/Smart-ATS-Resume-Optimizer.git
   cd Smart-ATS-Resume-Optimizer
   ```

2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   conda create -name venv python==3.10 -y
   conda activate venv
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables**:
   - Create a `.env` file in the project directory.
   - Add your Google API Key to the `.env` file:
     ```
     COHERE_API_KEY=your_cohere_api_key
     ```

### Running the Application

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Access the application at `http://localhost:8501` in your web browser.

## Usage

1. **Paste Job Description**: Copy and paste the job description in the provided text box.
2. **Upload Resume**: Upload your resume in PDF format.
3. **Choose Analysis Type**: Select one of the three options for ATS analysis.
   - **Percentage Match**: Get a percentage indicating the resume's match with the job description.
   - **Missing Skills**: Find out which skills or keywords are missing in the resume.
   - **Detailed Analysis**: Get an in-depth analysis including match percentage, missing skills, and a profile summary.

## Contact

For questions or feedback regarding the project, you can reach out to the project owner at [nikhilsinghxlx@gmail.com](mailto:nikhilsinghxlx@gmail.com).
