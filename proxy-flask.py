from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
CORS(app)

@app.route("/proxy", methods=["POST"])
@cross_origin()
def read_and_send():
        url = request.get_json()["url"]
        res = requests.get(url)
        html = res.text
        return Response(html, mimetype='text/html')

if __name__ == "__main__":
        app.run()
