from elasticsearch import Elasticsearch

def simpleQuery(query_body):
    elastic_client = Elasticsearch(hosts=["localhost"])
    result = elastic_client.search(index="kibana_sample_data_ecommerce", body=query_body)
    return result
