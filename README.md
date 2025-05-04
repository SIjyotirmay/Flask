# Flask
A personal repository to document and practice my journey with Flask, a lightweight Python web framework. This repo includes tutorials, mini-projects, experiments, and notes as I explore building web apps with Flask.

# app.py
Explanation:

Flask(__name__): Creates the Flask app.
@app.route(‘/’): Defines the home route (/).
def hello(): creates a function that is bound with ‘/‘ route and returns “HELLO” when the root page is accessed.
app.run(debug=True): runs the app in debug mode. It ensure that app is not need to restart manually if any changes are made in code.

# Build Flask Routes in Python
Web frameworks provide routing technique so that user can remember the URLs. It is useful to access the web page directly without navigating from the Home page. It is done through the following route() decorator, to bind the URL to a function.

@app.route(‘/hello’) 
def hello_world():     
    return ‘hello world’ 

If a user visits http://localhost:5000/hello URL, the output of the hello_world() function will be rendered in the browser.

# Variables in Flask ( It is passed as keyword argument.)
 from flask import Flask 
app = Flask(__name__) 

@app.route('/hello/<name>') 
def hello_name(name): 
    return 'Hello %s!' % name 

if __name__ == '__main__': 
    app.run(debug = True) 

parameter of route() decorator contains the variable part attached to the URL ‘/hello‘ as an argument. Hence, if URL like “http://localhost:5000/hello/GeeksforGeeks” is entered then “GeeksforGeeks” will be passed to the hello() function as an argument.

Besides the default string type, Flask also supports int, float, and path (which allows slashes for directories).

from flask import Flask 

app = Flask(__name__) 

@app.route('/blog/<int:postID>')
def show_blog(postID): 
    return 'Blog Number %d' % postID  

@app.route('/rev/<float:revNo>')
def revision(revNo): 
    return 'Revision Number %f' % revNo  

if __name__ == '__main__': 
    app.run(debug=True)

# Build a URL in Flask

from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/admin')  # decorator for route(argument) function
def hello_admin():  # binding to hello_admin call
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):  # binding to hello_guest call
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':  # dynamic binding of URL to function
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True)


# HTTP method are provided by Flask

GET:	This is used to send the data in an without encryption of the form to the server.

HEAD:	provides response body to the form

POST:	Sends the form data to server. Data received by POST method is not cached by server.

PUT:	Replaces current representation of target resource with URL.

DELETE:	Deletes the target resource of a given URL


# POST Method in Flask

The POST method is used to send data to the server for processing. Unlike GET, it does not append data to the URL. Instead, it sends data in the request body, making it a better choice for sensitive or large data.

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/square', methods=['GET', 'POST'])
def squarenumber():
    if request.method == 'POST':
        num = request.form.get('num')
        if num.strip() == '':   # Empty input
            return "<h1>Invalid number</h1>"
        square = int(num) ** 2
        return render_template('answer.html', squareofnum=square, num=num)
    return render_template('squarenum.html')

if __name__ == '__main__':
    app.run(debug=True)