from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)  # <-- THIS is the missing line

@app.route("/")
def index():
    df = pd.read_csv("../outputs/classified_resumes.csv")
    label_counts = df["Predicted Role"].value_counts()
    labels = label_counts.index.tolist()
    values = label_counts.values.tolist()

    return render_template(
        "index.jinja2",
        data=df,
        labels=labels,
        values=values
    )

if __name__ == "__main__":
    app.run(debug=True)


