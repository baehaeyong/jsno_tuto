from flask import Flask
from collections import Counter
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    user_string = '안녕 안녕 안녕 마 마 마 코딩 코딩 코딩 코딩'
    counter = dict(Counter(user_string))
    result = json.dumps(counter)

    return result

