from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>PBL-III Task 7: CI/CD with Jenkins + Docker + Kubernetes</h1><p>Version 1</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
