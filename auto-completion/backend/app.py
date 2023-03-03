from flask import Flask, request, jsonify
from generate import load_lstm,generate   
from torchtext.data.utils import get_tokenizer

import torch
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = get_tokenizer('spacy', language='en_core_web_sm')   


@app.route('/autocomplete', methods = ['GET','POST'])
def autocomplete():
    model,vocab_dict = load_lstm()
    sentence = request.json['sentence']
    temperature =  [0.4, 0.6, 0.8, 1.0]
    code = [' '.join(generate(sentence.strip(), 30, temp, model, tokenizer, vocab_dict, device, seed=0)) for temp in temperature]
    return jsonify({'predicted':code[-1]}), 201

