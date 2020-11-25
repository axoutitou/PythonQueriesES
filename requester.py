from elasticsearch import Elasticsearch

def getIndexPattern():
    elastic_client = Elasticsearch(hosts=["localhost"])
    result = elastic_client.indices.get_mapping("kibana_sample_data_ecommerce")
    return result


def simpleQuery(query_body):
    elastic_client = Elasticsearch(hosts=["localhost"])
    result = elastic_client.search(index="kibana_sample_data_ecommerce", body=query_body)
    return result