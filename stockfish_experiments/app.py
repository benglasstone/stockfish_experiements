from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../static/")

@app.route('/hello_world')
def hello_world():
    return 'No'

@app.route("/")
def index():
    return render_template("base.html")

if __name__ == '__main__':
    app.run()
