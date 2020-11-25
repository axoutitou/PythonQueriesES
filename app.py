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
        index_pattern = getIndexPattern()
        index = index_pattern['kibana_sample_data_ecommerce']['mappings']['properties']
        return render_template('index.html', result=result['hits']['total'], index=index)
        
    else :
        index_pattern = getIndexPattern()
        result = index_pattern['kibana_sample_data_ecommerce']['mappings']['properties']
        return render_template('index.html', index=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')