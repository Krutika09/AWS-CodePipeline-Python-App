from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

# @app.route('/Home')
# def home():
#     return 'Welcome to the Home page!'



if __name__ == '__main__':
    app.run()
