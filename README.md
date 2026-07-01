# 🚀 Smart ATS: Resume Optimization Tool

An AI-powered Resume Optimizer that analyzes your resume against a job description using Google's Gemini Large Language Model. The application provides an ATS compatibility score, identifies missing skills, and offers actionable suggestions to improve your chances of getting shortlisted.

---

## 📌 Features

* 📈 **ATS Match Score**

  * Calculates how closely your resume matches the job description.

* 🎯 **Missing Skills Detection**

  * Identifies important technical skills, tools, and keywords missing from your resume.

* 📊 **Detailed Resume Analysis**

  * Generates a comprehensive report including:

    * ATS Match Percentage
    * Missing Skills
    * Resume Strengths
    * Areas for Improvement
    * Professional Profile Summary

* 📄 **PDF Resume Support**

  * Upload resumes directly in PDF format.

* ⚡ **Powered by Google Gemini**

  * Uses Google's latest Gemini model for fast and accurate resume analysis.

---

## 🛠️ Tech Stack

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python            | Backend                         |
| Streamlit         | Web Application                 |
| Google Gemini API | AI Resume Analysis              |
| PyPDF2            | PDF Text Extraction             |
| python-dotenv     | Environment Variable Management |

---

## 📂 Project Structure

```text
Smart-ATS-Resume-Optimizer/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── assets/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Nickxlx/Smart-ATS-Resume-Optimizer.git

cd Smart-ATS-Resume-Optimizer
```

---

### 2. Create a Virtual Environment


Windows

```bash
conda create -n venv python==3.10 
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` File

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key
```

---

### 5. Get a Google Gemini API Key

1. Visit Google AI Studio.
2. Sign in with your Google account.
3. Generate an API key.
4. Copy it into the `.env` file.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit

```
http://localhost:8501
```

---

## 💡 How to Use

### Step 1

Paste the Job Description into the text area.

### Step 2

Upload your resume in PDF format.

### Step 3

Choose one of the available analyses:

* 📈 Percentage Match
* ⚠️ Missing Skills
* 📊 Detailed Resume Analysis

The AI will evaluate your resume and generate an ATS-friendly report.

---

## 📷 Demo

Upload a resume, paste a job description, and instantly receive:

* ATS Match Score
* Missing Keywords
* Resume Evaluation
* Improvement Suggestions

---

## 🚀 Future Enhancements

* Resume Improvement Suggestions
* Download Analysis as PDF
* Multiple Resume Comparison
* Support for DOCX Files
* Interactive ATS Dashboard
* Multi-LLM Support (Gemini, OpenAI, Groq, Ollama)

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Nikhil Singh**

* GitHub: https://github.com/Nickxlx
* LinkedIn: https://www.linkedin.com/in/nikhilsinghxlx/
* Email: [nikhilsinghxlx@gmail.com](mailto:nikhilsinghxlx@gmail.com)

---

⭐ If you found this project useful, consider giving it a star on GitHub!
