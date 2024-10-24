from creds import TOGETHER_AI_API_KEY
from helpers import TopRawMaterialStates
from flask import Flask,request
from flask_cors import CORS

api=Flask(__name__)
CORS(api)

@api.route('/')
def home():
    return 'welcome to seizo'

@api.route('/top5states')
def top5states():
    item = request.args.get('item')
    return TopRawMaterialStates(item)


api.run(debug=True)


