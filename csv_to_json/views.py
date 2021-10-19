from flask import Blueprint, render_template, request, flash, Response, jsonify
import pandas as pd

views = Blueprint('views', __name__)
from .csv_to_json_tree import ConvertCsvToJsonTree

ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@views.route('/', methods=['GET', 'POST'])
def index():
    """ This view function is used to display simple UI and upload csv file """
    if request.method == 'POST':

        try:
            """ Get the uploaded csv file data """
            csv_file = request.files["upload_csv_file"]

            """ Check the file extension is valid or not """
            if csv_file.filename == '':
                flash('Please upload file!', category='error')
            elif not allowed_file(csv_file.filename):
                flash('File is not CSV type!', category='error')
            else:
                # Read upload csv file data using pandas lib.
                csv_data = pd.read_csv(csv_file)
                # Remove all empty data
                csv_data = csv_data.dropna(how='all')

                """ Class ConvertCsvToJsonTree is used to create nested json data """
                csv_object = ConvertCsvToJsonTree(csv_data)
                out_json = csv_object.create_parent_tree()
                return Response(
                    out_json, mimetype='application/json',
                    headers={'Content-Disposition': 'attachment;filename=output.json'}
                )

        except Exception as e:
            flash(str(e), category='error')

    return render_template("index.html", user='')
