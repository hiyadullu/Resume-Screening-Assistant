def classify_resume(text):
    text = text.lower()
    if "python" in text and ("machine learning" in text or "data" in text):
        return "Data Science"
    elif "javascript" in text or "react" in text or "java" in text:
        return "Software Development"
    elif "recruitment" in text or "human resource" in text or "hiring" in text:
        return "HR"
    else:
        return "Other"
