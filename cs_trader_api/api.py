from flask import Flask, request, jsonify
from flask_cors import CORS
from config import config
import os

conf = config(os.path.join(os.path.dirname(__file__), "config.json"))

def create_api():
    api = Flask(__name__)
    CORS(api, resources={r"/*": {"origins": "*"}})
    api.config['SECRET_KEY'] = conf.get('secret_key')
    api.config['MAX_CONTENT_LENGTH'] = 15 * 1024 * 1024
    return api

api = create_api()

