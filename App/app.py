from flask import Flask, jsonify, request
import xmltodict as X
import time as T

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/get_xml", methods=['GET', 'POST'])
def parse_xml():
    start = T.time()
    xml_data = request.files['file']
    content_dict = X.parse(xml_data)
    end = T.time()
    time = end - start
    print(time)
    return jsonify(content_dict)

if __name__ == '__main__':
    print("Starting python app")
    app.run(host='0.0.0.0', port=8080, debug=True)