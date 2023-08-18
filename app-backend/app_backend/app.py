from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! We are Live!'

if __name__ == "__main__":
    app.run(debug=True)
#
# while True:
#     print("hello")