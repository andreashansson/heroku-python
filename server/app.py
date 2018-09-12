import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.jsonify({"test": "test"})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
