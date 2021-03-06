import flask

app = flask.Flask(__name__, static_folder="build/static", template_folder="build/")

@app.route("/")
def index():
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
