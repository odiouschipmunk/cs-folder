from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
import pathlib
import os
import requests
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import Functions
from better_profanity import profanity
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
import hashlib
def md5_hash(text, *args):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

app = Flask(__name__)
import secrets
app.secret_key = secrets.token_hex(16)  # Replace with a real secret key
app.jinja_env.filters['hash'] = md5_hash
from dotenv import load_dotenv
load_dotenv()
# Google OAuth2 Configuration
GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']  # Replace with your client ID
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)

class User(UserMixin):
    def __init__(self, user_id, email, name):
        self.id = user_id        # This will be the 'sub' from Google
        self.email = email
        self.name = name

@login_manager.user_loader
def load_user(user_id):
    if 'user_info' not in session:
        return None
    user_info = session['user_info']
    return User(
        user_id=user_info.get('sub'),  # Changed from 'id' to 'sub'
        email=user_info.get('email'),
        name=user_info.get('name')
    )

@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

# Inside the /callback route, update the token verification:
@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID,
        clock_skew_in_seconds=60  # Allow a 60 second clock skew
    )

    # Debugging: print the id_info dictionary
    print(id_info)

    # Ensure the required fields are present
    if 'sub' not in id_info or 'email' not in id_info or 'name' not in id_info:
        return "Invalid token", 400

    # Store the complete id_info in session
    session['user_info'] = id_info
    
    # Create user with 'sub' as the ID
    user = User(
        user_id=id_info['sub'],
        email=id_info.get('email'),
        name=id_info.get('name', 'Anonymous User')
    )
    
    login_user(user)
    return redirect(url_for('index'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('index'))

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
        return redirect(url_for("thanks", teacher=teacher))
    return render_template("index.html", teachers=teachers, user=current_user)

# Update all routes to require login
@app.route("/get_teachers")
@login_required
def get_teachers_route():
    teachers = Functions.get_teachers()
    return jsonify(teachers)

@app.route("/thanks")
@login_required
def thanks():
    teacher = request.args.get('teacher')
    return render_template("thanks.html", teacher=teacher)

@app.route("/feedback", methods=["GET"])
@login_required
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
@login_required
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
