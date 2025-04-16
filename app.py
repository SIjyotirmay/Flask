from flask import Flask
app = Flask(__name__)

@app.route('/')
def print_hello_world():
    return "hello world!!!"

if __name__ == "__main__":
    app.run(debug=True, port = 8000)