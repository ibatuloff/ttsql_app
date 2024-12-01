from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    text = request.form['text']
    processed_text = text.capitalize()
    return welcome(processed_text)

@app.route('/welcome')
def welcome(name=None):
    return render_template('welcome.html', name=name)

@app.route('/get', methods=['GET'])
def index_get():
    return f"You sent get request. Here is response. Now what?"

with app.test_request_context():
    print(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')