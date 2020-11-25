from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    #if request.method == 'POST' :
    #    details = request.form
    #    result = machineLearningPrediction(details['phrase'])
    #    return render_template('index.html', result=result)
        
    #else :
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')