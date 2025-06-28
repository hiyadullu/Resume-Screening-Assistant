import os
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import pdfplumber
import fitz

UPLOAD_FOLDER = 'uploads'


app = Flask(__name__)  
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
#filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

TARGET_KEYWORDS = {
    "Data Science": ["machine learning", "data analysis", "python", "pandas", "statistics"],
    "Software Development": ["java", "python", "git", "api", "sql", "docker"],
    "HR": ["recruiting", "onboarding", "employee engagement", "compliance", "payroll"]
}

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()


def match_keywords(text):
    scores = {}
    for category, keywords in TARGET_KEYWORDS.items():
        matched = [kw for kw in keywords if kw in text]
        scores[category] = {
            "matched": matched,
            "match_percent": int(len(matched) / len(keywords) * 100)
        }
    return scores


@app.route('/upload', methods=["GET", "POST"])
def upload_resume():
    if 'resume' not in request.files:
        return "No file uploaded", 400

    file = request.files['resume']
    if file.filename == '':
        return "No selected file", 400

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Parse PDF text
        with fitz.open(filepath) as doc:
            text = ''
            for page in doc:
                text += page.get_text()

        # Simple keyword matching
        if "python" in text.lower():
            category = "Software Development"
        elif "recruitment" in text.lower() or "hiring" in text.lower():
            category = "Human Resources"
        elif "data analysis" in text.lower() or "machine learning" in text.lower():
            category = "Data Science"
        else:
            category = "Uncategorized"

        return render_template("index.jinja2", result=f"Resume categorized as: {category}")

    return "Upload failed", 500

@app.route("/", methods=["GET", "POST"])
def index():
    df = pd.read_csv("../outputs/classified_resumes.csv")
    label_counts = df["Predicted Role"].value_counts()
    labels = label_counts.index.tolist()
    values = label_counts.values.tolist()
    results= None
    if request.method == 'POST':
        file = request.files['resume']
        if file and file.filename.endswith('.pdf'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            resume_text = extract_text_from_pdf(filepath)
            results = match_keywords(resume_text)

    return render_template(
        "index.jinja2",
        data=df,
        labels=labels,
        values=values,
        results=results,
    )
    
if __name__ == "__main__":
    app.run(debug=True)



