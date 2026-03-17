from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

questions = [
    {
        "question": "What does DNS stand for?",
        "options": ["Domain Name System", "Data Network Service", "Digital Name Server", "Dynamic Network System"],
        "answer": "Domain Name System"
    },
    {
        "question": "Which cloud service is used for containers?",
        "options": ["EC2", "S3", "Kubernetes", "Lambda"],
        "answer": "Kubernetes"
    },
    {
        "question": "Which DevOps tool is used for CI/CD?",
        "options": ["Docker", "Jenkins", "Terraform", "Ansible"],
        "answer": "Jenkins"
    },
    {
        "question": "Which port does HTTP use?",
        "options": ["21", "22", "80", "443"],
        "answer": "80"
    },
    {
        "question": "Terraform is mainly used for?",
        "options": ["Monitoring", "Infrastructure as Code", "Logging", "Networking"],
        "answer": "Infrastructure as Code"
    }
]

@app.route('/')
def home():
    return render_template("index.html", questions=questions)

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    score = 0

    for i, q in enumerate(questions):
        if data[str(i)] == q["answer"]:
            score += 1

    return jsonify({"score": score})

if __name__ == "__main__":
    app.run(debug=True)