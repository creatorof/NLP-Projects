from flask import Flask, jsonify, request
from utils import resume_parser
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/skills')
def get_skills():
    return jsonify(['c','python','jira'])



@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    files = request.files.get("file")
    result = resume_parser(files)
    return jsonify(result), 201




