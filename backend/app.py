from flask import Flask, render_template, url_for, request

app = Flask(__name__, static_folder='../static')

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None 
    if request.method == 'POST':
        print(request.args)
        text = request.form['text']
        processed_text = text.capitalize()
        return response(processed_text)
    return render_template('index.html')

@app.route('/response')
def response(text=None):
    return render_template('response.html', text=text)

@app.route('/get', methods=['GET'])
def index_get():
    return f"You sent get request. Here is response. Now what?"

with app.test_request_context():
    print(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')