from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route('/generateReport', methods=['POST'])
def generate_report():
    csv = request.files['file']
    df = pd.read_csv(csv)
    df = df.select_dtypes(include="number") # drop non-numeric columns

    report = {}
    for column in df.columns:
        stats = {}
        stats["min_value"] = df[column].min()
        stats["max_value"] = df[column].max()
        stats["mean"] = df[column].mean()
        stats["standard_deviation"] = df[column].std()
        stats["kurtosis"] = df[column].kurt()
        report[column] = stats

    return report

if __name__ == '__main__':
    app.run(port=10000)