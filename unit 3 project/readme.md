# Teacher Review Website Documentation

To run this program, you'll need Python installed on your computer. You'll also need to install Flask, which you can do by typing "pip install flask" in the terminal. Once Flask is installed, go to the project folder in your terminal and type "python app.py" to start the website. Then open your web browser and go to http://localhost:5000 to see the website.

When you open the website, you'll see the main page with a form. The form has a dropdown menu where you can select a teacher, another dropdown that shows the courses for that teacher, and a text box where you can write your review. After writing your review, click the submit button to save it. If you want to read other reviews, click on "View Reviews" where you can select a teacher and see what others have written about them.

The website uses two main program files. The first file, app.py, contains functions that handle the website pages and user interactions. The index() function shows the main page and handles review submissions. The get_teachers_route() function provides the list of teachers and their courses. The thanks() function shows a confirmation page after submitting a review. The feedback() function displays reviews for a specific teacher and course, and the view_reviews() function shows all reviews for a selected teacher.

The second file, Functions.py, manages how data is stored and retrieved. It includes init_csv() which creates the necessary files when first running the program, get_teachers() which reads teacher and course information, read_reviews() which gets all saved reviews, write_review() which saves new reviews, and show_reviews() which finds reviews for a specific teacher.
