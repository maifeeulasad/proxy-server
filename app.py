from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
import requests
import os

port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
CORS(app)

@app.route("/proxy", methods=["POST"])
@cross_origin()
def read_and_send():
        url = request.get_json()["url"]
        res = requests.get(url)
        html = res.text
        return Response(html, mimetype='text/html')

@app.route("/", methods=["GET"])
def readme():
        with open('./README.md','r') as readme:
                return Response(readme.read(), mimetype='text/markdown')

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=port, debug = True)
