from flask import Flask, render_template, request, redirect, url_for, jsonify
import csv
from pathlib import Path

app = Flask(__name__)


# Initialize CSV file if it doesn't exist
def init_csv():
    if not Path("teacher_reviews.csv").exists():
        with open("teacher_reviews.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["review", "teacher", "class"])


# Read existing reviews
def read_reviews():
    reviews = []
    with open("teacher_reviews.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        reviews = list(reader)
    return reviews


# Write a new review
def write_review(review):
    with open("teacher_reviews.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(review)


# Read teacher data from CSV
def get_teachers():
    teachers = {}
    try:
        with open("teacher_data.csv", "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                teacher_name = row.get("Teacher", "").strip()
                course_name = row.get("Course Name", "").strip()
                if teacher_name and course_name:
                    if teacher_name not in teachers:
                        teachers[teacher_name] = set()
                    teachers[teacher_name].add(course_name)
        # Convert sets to sorted lists
        for teacher in teachers:
            teachers[teacher] = sorted(teachers[teacher])
        return teachers
    except Exception as e:
        print(f"Error reading teacher data: {e}")
        return {}


@app.route("/", methods=["GET", "POST"])
def index():
    init_csv()
    teachers = get_teachers()
    if request.method == "POST":
        teacher = request.form["teacher"]
        course = request.form["course"]
        message = request.form["message"]
        write_review([message, teacher, course])
        return redirect(url_for("thanks"))
    return render_template("index.html", teachers=teachers)


@app.route("/get_teachers")
def get_teachers_route():
    teachers = get_teachers()
    return jsonify(teachers)


@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

    @app.route("/feedback", methods=["GET"])
    def feedback():
        teacher = request.args.get("teacher")
        course = request.args.get("course")
        reviews = read_reviews()
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
