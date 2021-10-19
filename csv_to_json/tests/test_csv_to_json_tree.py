from flask import Flask, Request, request
from io import BytesIO
import json
import pandas as pd

from csv_to_json.csv_to_json_tree import ConvertCsvToJsonTree

RESULT = False
ALLOWED_EXTENSIONS = {'csv'}


class FileObj(BytesIO):

    def close(self):
        global RESULT
        RESULT = True


class MyRequest(Request):
    def _get_file_stream(*args, **kwargs):
        return FileObj()


app = Flask(__name__)
app.debug = True
app.request_class = MyRequest


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class TestConvertCsvToNestedJson:

    def test_file_upload_case(self):

        @app.route("/upload", methods=['POST'])
        def upload():
            csv_file = request.files['file']
            print('in upload handler')
            if not allowed_file(csv_file.filename):
                print('File is not CSV type')
                assert False
            else:
                assert isinstance(
                    csv_file.stream,
                    FileObj,
                )
                return 'ok'

        client = app.test_client()
        resp = client.post(
            '/upload', buffered=True,
            data={
                'file': (BytesIO(b'FILE CONTENT'), 'sample_data.csv'),
            },
            content_type='multipart/form-data'
        )

        assert b'ok' == resp.data

    def test_create_nested_tree(self):

        # Read upload csv file data using pandas lib.
        csv_data = pd.read_csv("csv_to_json/tests/sample_data.csv")
        # Remove all empty data
        csv_data = csv_data.dropna(how='all')

        """ Class ConvertCsvToJsonTree is used to create nested json data """
        csv_object = ConvertCsvToJsonTree(csv_data)
        out_json = csv_object.create_parent_tree(is_dump_with_indent=False)

        with open('csv_to_json/tests/output.json', 'r') as json_file:
            out_data = json.load(json_file)
        assert out_json == out_data
