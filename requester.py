from elasticsearch import Elasticsearch

def getIndexPattern():
    elastic_client = Elasticsearch(hosts=["localhost"])
    result = elastic_client.indices.get_mapping("kibana_sample_data_ecommerce")
    return result


def simpleQuery(query_body):
    elastic_client = Elasticsearch(hosts=["localhost"])
    result = elastic_client.search(index="kibana_sample_data_ecommerce", body=query_body)
    return result

def launchStringToDictionnary(test_str) :
    test_str = test_str.replace("\r\n", "")
    test_str = test_str.replace("\"", "")
    return  stringToDictionnary(test_str)
 
def stringToDictionnary(test_str):
    if ":" not in test_str:
        return test_str

    item = test_str.split(":",1)
    if "{" in item[1]:
        val = item[1].split("{", 1)
        tmp = "".join(val[1:])
        return {item[0].strip() : stringToDictionnary(tmp)}
    else :
        val = item[1].split("}", 1)
        return  {item[0].strip() : val[0].strip()}