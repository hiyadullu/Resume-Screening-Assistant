# Resume Screening Assistant

An automated Python tool that classifies resumes into job categories like **Data Science**, **Software Development**, and **HR** by analyzing keywords in PDF files.

##  Goal
- Reduce manual effort in shortlisting resumes
- Automatically group resumes based on job roles
- Output a report as a `.csv` file

##  Tools Used
- Python
- PyPDF2
- Pandas

##  How it works
- Extracts text from PDF resumes
- Uses simple keyword-based logic to assign job categories
- Saves the result in `classified_resumes.csv`

##  Folder Structure
Resume-Screening-Assistant/
├── resumes/ # Folder with PDF resumes
├── outputs/ # CSV file will be saved here
├── scripts/
│ ├── resume_parser.py
│ ├── classifier.py
│ └── main.py
├── requirements.txt
└── README.md


