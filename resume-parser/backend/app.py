from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]

@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)



@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    files = request.files.get("file")
    print(files)
    return jsonify("Success"), 204

