from flask import Flask, render_template, request, redirect, url_for, jsonify
import Functions
from better_profanity import profanity
from transformers import pipeline
import numpy as np

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
        #truncate the message to only 50k chars
        message = message[:50000]
        #print(generate_rating(message))
        Functions.write_review([message, teacher, course])
        return redirect(url_for("thanks", teacher=teacher))
    return render_template("index.html", teachers=teachers)


@app.route("/get_teachers")
def get_teachers_route():
    teachers = Functions.get_teachers()
    return jsonify(teachers)

def generate_rating(message):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(message)
    rating=[result[0]['label'], result[0]['score']]
    #generate a numerical rating from 1-5
    num=0
    if rating[0]=='POSITIVE':
        num=rating[1]
    if rating[0]=='NEGATIVE':
        num=-rating[1]
    
    num = 4 * (1 / (1 + np.exp(-num)))
    return int(num)

@app.route("/thanks")
def thanks():
    teacher = request.args.get('teacher')
    return render_template("thanks.html", teacher=teacher)

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

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
