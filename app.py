from flask import Flask, render_template
from werkzeug.exceptions import abort
import helper

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/<value_id>', methods=['GET', 'POST'])
def show_value(value_id: str):
    value_obj = helper.fetch_value(value_id)
    if value_obj is None:
        abort(404)
    p_tag = '<p> %s </p>' % value_obj[1]
    return render_template('value.html', value_id=value_id, value=p_tag)

@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')
