from flask import Flask, request, render_template, redirect
from concurrent.futures import ThreadPoolExecutor
from handlers import request_exception_handler
import os
import json

DOCUMENT_NAMES = ["agreement", "cmd", "contract", "invoice"]
SITE_LOCATION = os.path.join("..", "ED-site")
STATIC_FILE_LOCATION = os.path.join("..", "ED-site", "CSS")
executor = ThreadPoolExecutor(4)

app = Flask(__name__, template_folder=SITE_LOCATION)


def add_document(name):
    return "Document {} added successfully!".format(name)


@app.route("/")
@request_exception_handler
def index():
    return redirect('/easy_declare.html')


@app.route('/<path:subpath>')
@request_exception_handler
def show_subpath(subpath):
    print(subpath)
    return render_template(subpath)


@app.route("/post_agreement", methods=['POST'])
@request_exception_handler
def post_agreement():
    print(request)
    add_document("agreement")


@app.route("/post_cmr", methods=['POST'])
@request_exception_handler
def post_cmr():
    print(request)
    add_document("cmr")


@app.route("/post_contract", methods=['POST'])
@request_exception_handler
def post_contract():
    print(request)
    add_document("contract")


@app.route("/post_invoice", methods=['POST'])
@request_exception_handler
def post_invoice():
    print(request)
    add_document("invoice")


@app.route("/post_test", methods=['POST'])
@request_exception_handler
def post_test():
    return str(request)


@app.route("/get_test", methods=['GET'])
@request_exception_handler
def get_test():
    return str(request)


@app.route("/get_json", methods=['GET'])
@request_exception_handler
def get_json():
    print(request)
    json_path = os.path.join("..", "Documents", "all_fields.json")
    if os.path.exists(json_path):
        with open(json_path) as jp:
            json_to_give = json.load(jp)
    return json.dumps(json_to_give)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)