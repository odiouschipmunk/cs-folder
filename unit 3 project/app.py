from flask import Flask, render_template, request, redirect, url_for, jsonify
import Functions
from better_profanity import profanity

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    Functions.init_csv()
    teachers = Functions.get_teachers()
    if request.method == "POST":
        teacher = request.form["teacher"]
        course = request.form["course"]
        message = request.form["message"]
        message = profanity.censor(message)
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


@app.route('/view_reviews', methods=['GET', 'POST'])
def view_reviews():
    Functions.init_csv()
    if request.method == 'POST':
        teacher = request.form['teacher']
        filtered_reviews=Functions.show_reviews(teacher)
        return render_template('view_reviews.html', teacher=teacher, reviews=filtered_reviews)
    else:
        teachers = Functions.get_teachers()
        return render_template('select_teacher.html', teachers=teachers)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
