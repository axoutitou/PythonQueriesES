from flask import Flask, request, render_template
from requester import *
from json import dumps

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' :
        details = request.form
        query = launchStringToDictionnary(details['query'])
        result = simpleQuery(query)
        index_pattern = getIndexPattern()
        index = index_pattern['kibana_sample_data_ecommerce']['mappings']['properties']
        rendered_result = dumps(result, indent=4, separators=(',', ': '))
        rendered_query = dumps(query, indent=4, separators=(',', ': '))
        return render_template('index.html', query=rendered_query, result=rendered_result, index=index)
        
    else :
        index_pattern = getIndexPattern()
        result = index_pattern['kibana_sample_data_ecommerce']['mappings']['properties']
        return render_template('index.html', index=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')