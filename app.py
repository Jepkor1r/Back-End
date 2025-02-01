
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)

#Enable CORS for all routes
CORS(app)

@app.route('/api/info', methods=['GET'])
def get_info():

    # Handle the actual GET request 
    data = {
    "email": "jlagat007@gmail.com",
    "current_datetime": datetime.utcnow().isoformat() + "Z",
    "github_url": "https://github.com/Jepkor1r/Back-End"
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)