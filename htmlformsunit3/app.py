from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
