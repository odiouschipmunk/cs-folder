from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return 'hello world'

@app.route('/im-amazing')
def im_amazing():
    return 'i am defintely amazing'
if __name__ == '__main__':
   app.run(debug = True, port=5000)
