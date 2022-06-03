from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():

    dna_img = url_for('static', filename='images/dna.png')
    return render_template('index.html', output_img=dna_img)


if __name__ == "__main__":
    app.run(debug=False)


# debug is set to false which was true and also not hosting port was specified....all these are done just for hosting purposes so change it with change in needs.
