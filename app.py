from flask import Flask
from flask_cors import CORS
from flask import jsonify
from datetime import datetime

app = Flask(__name__)

#Enable CORS for all routes and all origins
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/info', methods=['GET'])
def get_info():

    data = {
    "email": "jlagat007@gmail.com",
    "current_datetime": datetime.utcnow().isoformat() + "Z",
    "github_url": "https://github.com/Jepkor1r/Back-End"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)