from flask import Flask, request, render_template, redirect, send_file
from concurrent.futures import ThreadPoolExecutor
from handlers import request_exception_handler
import json
import os

os.chdir(".")

DOCUMENT_NAMES = ["agreement", "cmr", "contract", "invoice"]
ALLOWED_EXTENSIONS = set(['doc', 'docx'])
SITE_LOCATION = os.path.join("..", "ED-site")
DOC_LOCATION = os.path.join("..", "Documents")
STATIC_FILE_LOCATION = os.path.join("..", "ED-site", "CSS")
executor = ThreadPoolExecutor(4)


app = Flask(__name__, template_folder=SITE_LOCATION, static_folder=SITE_LOCATION)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def add_document(name):
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file.save(os.path.join(DOC_LOCATION, name + '.docx'))
            return redirect(url_for('add_document', name + '.docx'))


def parse_documents():
    convert_bootstrap.collect_data()


@app.route("/")
@request_exception_handler
def index():
    print(request)
    return render_template('/Easy_Declare.html')


@app.route('/<path:subpath>')
@request_exception_handler
def show_subpath(subpath):
    print(subpath)
    if subpath.endswith(".html"):
        return render_template(subpath)
    else:
        return app.send_static_file(subpath)


@app.route('/post_agreement', methods=['POST'])
@request_exception_handler
def post_agreement():
    print(request)
    add_document('agreement')


@app.route('/post_cmr', methods=['POST'])
@request_exception_handler
def post_cmr():
    print(request)
    add_document('cmr')


@app.route('/post_contract', methods=['POST'])
@request_exception_handler
def post_contract():
    print(request)
    add_document('contract')


@app.route('/post_invoice', methods=['POST'])
@request_exception_handler
def post_invoice():
    print(request)
    add_document('invoice')


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
    return str(json_to_give)


@app.route("/get_xlsx", methods=['GET'])
@request_exception_handler
def get_xlsx():
    print(request)
    return send_file("_result.xlsx", as_attachment=True)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
