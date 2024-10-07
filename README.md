# Smart ATS: Resume Optimization Tool

## Project Overview
The **Smart ATS: Resume Optimization Tool** is an interactive application designed to enhance resumes for Applicant Tracking Systems (ATS). This tool analyzes a resume against a job description (JD), providing insights into how well the resume matches the job requirements. The analysis is done using **Google's Gemini-Pro Generative AI** model to ensure precise and accurate results.

## Features
- **Percentage Match**: Calculates the percentage match between the uploaded resume and the job description.
- **Missing Skills**: Identifies skills and keywords from the job description that are absent in the resume.
- **Detailed Analysis**: Provides a comprehensive analysis, including a match percentage, missing keywords, and a profile summary based on the resume.

## Tech Stack
- **Streamlit**: For creating the web interface.
- **Google Generative AI (Gemini-Pro)**: For generating responses based on the provided resume and job description.
- **PyPDF2**: For extracting text from uploaded PDF resumes.
- **dotenv**: For securely managing API keys and environment variables.

## How It Works
1. **Upload a Resume**: Upload a PDF version of the resume.
2. **Paste the Job Description**: Paste the job description into the provided text box.
3. **Select an Analysis Option**:
   - **Percentage Match**: Evaluates how closely the resume matches the job description.
   - **Missing Skills**: Identifies key skills or qualifications missing in the resume.
   - **Detailed Analysis**: Provides a full report including match percentage, missing skills, and a profile summary.

## Setup Instructions

### Prerequisites
Make sure you have the following installed:
- Python 3.9 or 3.10
- Streamlit
- Google Generative AI library
- PyPDF2
- dotenv

### Installation

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
     GOOGLE_API_KEY=your_google_api_key
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