from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route("/proxy", methods=["POST"])
def read_and_send():
        url = request.get_json()["url"]
        res = requests.get(url)
        html = res.text
        return Response(html, mimetype='text/html')

#print(read_and_send("https://www.cnn.com/2022/11/14/business/jeff-bezos-charity/index.html"))

if __name__ == "__main__":
        app.run()
