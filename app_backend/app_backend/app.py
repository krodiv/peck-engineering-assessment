from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! We are Live!'

if __name__ == "__main__":
    app.run(debug=True) # this is a development server run not a production level deployment