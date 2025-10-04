from flask_cors import CORS
from flask import Flask, jsonify
import random

app = Flask(__name__)
CORS(app)

# Vercel Python serverless function entrypoint
# See: https://vercel.com/docs/functions/python

def handler(request):
    colors = ["red", "green", "violet"]
    weights = [0.45, 0.45, 0.10]
    result = random.choices(colors, weights=weights, k=1)[0]
    return jsonify({"result": result})
