from flask import Flask, request, jsonify
import translate
from flask_cors import CORS, cross_origin




app = Flask(__name__)
cors = CORS(app)


@app.route('/translate', 'POST')
def translate_to_en():
    source = request.json['sentence']
    translatedText = translate(source)
   
    result = {"source":source, "predict":translatedText}
    return jsonify(result), 201
