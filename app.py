from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world!\n my name is Jyotirmay Shrestha"

if __name__ =="__main__":
    app.run(debug=True)