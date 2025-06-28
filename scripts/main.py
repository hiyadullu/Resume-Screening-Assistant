import os
import pandas as pd
from resume_parser import parse_all_resumes
from classifier import classify_resume

RESUME_FOLDER = "./resumes/"
OUTPUT_FILE = "./outputs/classified_resumes.csv"

resumes = parse_all_resumes(RESUME_FOLDER)

results = []

for filename, text in resumes.items():
    role = classify_resume(text)
    results.append({"File": filename, "Predicted Role": role})

df = pd.DataFrame(results)
os.makedirs("outputs", exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

print("Classification complete. Results saved to classified_resumes.csv")
