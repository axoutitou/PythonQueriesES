from flask import Flask, request, render_template
from requester import *

app = Flask(__name__)
query = {
    "query":{
        "match":{
            "customer_full_name":"Tariq Rivera"
        }
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' :
        details = request.form
        result = simpleQuery(query)
        return render_template('index.html', result=result['hits']['total'])
        
    else :
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')