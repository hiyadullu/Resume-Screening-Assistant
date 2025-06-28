# Resume Analyzer Web App

A simple Flask-based web application that classifies uploaded resumes into predefined job roles based on keyword matching.

---

## Table of Contents

1. Introduction  
2. Objective  
3. Tech Stack  
4. Features  
5. How It Works  
6. Screenshots  
7. Installation  
8. Project Structure  
9. Challenges Faced  
10. Contributors  
11. License  
12. Project Links  

---

## Introduction

This web app allows users to upload a PDF resume, from which it extracts text and evaluates how well it matches specific job domains such as:

- Data Science  
- Software Development  
- Human Resources (HR)  

It uses keyword matching to suggest the most relevant job category based on resume content.

---

## Objective

To streamline the initial screening process in recruitment by building a lightweight system that:
- Parses PDF resumes
- Matches them against relevant domain keywords
- Classifies them into appropriate job categories

---

## Tech Stack

| Component         | Tech Used             |
|------------------|-----------------------|
| Backend Framework | Flask (Python)        |
| PDF Processing    | pdfplumber, PyMuPDF   |
| Frontend          | HTML, CSS, Jinja2     |
| Data Handling     | pandas                |
| IDE               | VS Code               |

---

## Features

- Upload resume in PDF format
- Keyword-based classification into job roles
- Match percentage calculation
- Result display with visual feedback
- Optionally logs data into CSV for later analysis

---

## How It Works

1. User uploads a resume (PDF).
2. Text is extracted from the file.
3. Extracted text is converted to lowercase and compared to a list of predefined keywords for each category.
4. Based on keyword matches, the system selects the best-fit job category.
5. Result is rendered back to the user, optionally with percentage match.

---

## Installation

Step-by-step to run the app locally:

git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
python app.py


Visit the app in your browser at `http://127.0.0.1:5000`

---

## Project Structure

## Project Structure

- **resume-analyzer/**
  - **templates/**
    - `index.jinja2` – Main frontend page
  - **uploads/** – Uploaded resume PDFs
  - **outputs/**
    - `classified_resumes.csv` – Output logs
  - `app.py` – Flask application
  - `requirements.txt`
  - `README.md`

---

## Challenges Faced

| Issue | Solution |
|-------|----------|
| Text extraction failed for some PDFs | Used PyMuPDF (`fitz`) as a fallback to `pdfplumber` |
| POST method error | Ensured correct Flask route method declarations |
| Inconsistent parsing | Standardized lowercase matching and cleaned input |

---

## License

This project is licensed under the MIT License.




