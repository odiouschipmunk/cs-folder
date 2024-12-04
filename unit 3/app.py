from flask import Flask, render_template, request, redirect, url_for, jsonify
from . import Functions
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    Functions.init_csv()
    teachers = Functions.get_teachers()
    if request.method == "POST":
        teacher = request.form["teacher"]
        course = request.form["course"]
        message = request.form["message"]
        Functions.write_review([message, teacher, course])
        return redirect(url_for("thanks"))
    return render_template("index.html", teachers=teachers)


@app.route("/get_teachers")
def get_teachers_route():
    teachers = Functions.get_teachers()
    return jsonify(teachers)


@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

@app.route("/feedback", methods=["GET"])
def feedback():
    teacher = request.args.get("teacher")
    course = request.args.get("course")
    reviews = Functions.read_reviews()
    filtered_reviews = [
        review
        for review in reviews
        if review["teacher"] == teacher and review["class"] == course
    ]
    return render_template(
        "feedback.html", teacher=teacher, course=course, reviews=filtered_reviews
    )



if __name__ == "__main__":
    app.run(debug=True)
