from flask import Flask, render_template, request, redirect, url_for
from blockchain import write_block, check_integrity


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html', blocks=check_integrity())
    name = request.form.get("name")
    surname = request.form.get("surname")
    replica = request.form.get("replica")
    write_block(name, surname, replica)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
