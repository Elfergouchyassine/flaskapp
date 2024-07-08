from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to my first flask app!'

@app.route('/about')
def about():
    return 'This is simple flask app created by me'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
