from flask import Flask, request, jsonify
import translate
from flask_cors import CORS, cross_origin




app = Flask(__name__)
cors = CORS(app)


@app.route('/translate', methods=['POST'])
def translate_to_en():
    source = request.json['source']
    print(source)
    translatedText = translate(source)
    translated_text = "I am not alright"
    result = {"source":source, "translated_text":translated_text}
    return jsonify(result), 201
