from csv_to_json import create_app
import sys

app = create_app()

ROOT_PATH = sys.path.insert(0, '..')

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['ROOT_PATH'] = ROOT_PATH
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
