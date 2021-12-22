from flask import Flask, render_template, request
app = Flask(__name__)
from covid import testData
@app.route('/')
def index():
    return render_template('TESTYOURSELF.html')
    
    
@app.route('/results', methods= ["POST"])
def submit():
    if request.method == 'POST':
        input_dict = request.form
        input_data = tuple(input_dict.values())
        result = testData(input_data)
        return render_template('results.html',n = result)
if __name__ == '__main__':
    app.run()

