from flask import Flask, request
from concurrent.futures import ThreadPoolExecutor
from handlers import request_exception_handler

DOCUMENT_NAMES = ["agreement", "cmd", "contract", "invoice"]
executor = ThreadPoolExecutor(4)

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, this is a customs declaration app! Put 4 documents here."

@app.route("/test_container")
def another_site():
    return "Hello, this is a new webpage."

def add_document(name):
    return "Document {} added successfully!".format(name)


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


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
