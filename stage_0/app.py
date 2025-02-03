from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)

@app.get("/api/user")
def getUser():
    current_datetime = datetime.utcnow()
    response ={
            "email": "greymobley86@gmail.com",
            "current_datetime": current_datetime.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "github_url": "https://github.com/EmmanuelNiyonshuti/hng-internship-projects"
        }
    return jsonify(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
