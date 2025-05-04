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