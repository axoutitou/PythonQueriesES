from elasticsearch import Elasticsearch

query1= { "query": {
            "query_string": {
                    "fields": [
                        "category"
                    ],
                "query": "Women's Shoes",
                "minimum_should_match": 2
                }
            },
            "fields": [
                "customer_full_name",
                "manufacturer",
                "customer_gender"
            ],
            "_source": "false"
        }

query2= {  
        "query": {
            "query_string": {
                "fields": [
                    "order_date"
                ],
            "query": "2020-12",
            "minimum_should_match": 2
            }
        },
        "fields": [
            "customer_full_name",
            "customer_gender",
            "category",
            "products.product_name",
            "order_date"
        ],
        "_source": "false"
    }  

query3= {
    "query": {
        "prefix": {
            "customer_first_name": "b"
        }
    },
    "fields": [
        "customer_first_name",
        "customer_gender"
    ],
    "_source": "false"
}

query4 = {
  "aggs": {
    "2": {
      "date_histogram": {
        "field": "order_date",
        "calendar_interval": "1y",
        "time_zone": "Europe/Paris",
        "min_doc_count": 1
      },
      "aggs": {
        "3": {
          "terms": {
            "field": "customer_gender",
            "order": {
              "_count": "desc"
            },
            "size": 5
          }
        }
      }
    }
  },
  "size": 0,
  "stored_fields": [
    "*"
  ],
  "script_fields": {},
  "docvalue_fields": [
    {
      "field": "customer_birth_date",
      "format": "date_time"
    },
    {
      "field": "order_date",
      "format": "date_time"
    },
    {
      "field": "products.created_on",
      "format": "date_time"
    }
  ],
  "_source": {
    "excludes": []
  },
  "query": {
    "bool": {
      "must": [],
      "filter": [
        {
          "match_all": {}
        },
        {
          "range": {
            "order_date": {
              "gte": "2020-12-01T17:25:53.895Z",
              "lte": "2020-12-01T17:40:53.895Z",
              "format": "strict_date_optional_time"
            }
          }
        }
      ],
      "should": [],
      "must_not": []
    }
  }
}

query5 = {
  "aggs": {
    "2": {
      "terms": {
        "field": "manufacturer.keyword",
        "order": {
          "_key": "desc"
        },
        "size": 5
      },
      "aggs": {
        "1": {
          "avg": {
            "field": "products.min_price"
          }
        }
      }
    }
  },
  "size": 0,
  "stored_fields": [
    "*"
  ],
  "script_fields": {},
  "docvalue_fields": [
    {
      "field": "customer_birth_date",
      "format": "date_time"
    },
    {
      "field": "order_date",
      "format": "date_time"
    },
    {
      "field": "products.created_on",
      "format": "date_time"
    }
  ],
  "_source": {
    "excludes": []
  },
  "query": {
    "bool": {
      "must": [],
      "filter": [
        {
          "match_all": {}
        },
        {
          "match_phrase": {
            "manufacturer.keyword": "Elitelligence"
          }
        },
        {
          "range": {
            "order_date": {
              "gte": "2020-12-01T17:56:24.885Z",
              "lte": "2020-12-01T18:11:24.885Z",
              "format": "strict_date_optional_time"
            }
          }
        }
      ],
      "should": [],
      "must_not": []
    }
  }
}

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
		
def setQueryExamples(query_index) :
    elastic_client = Elasticsearch(hosts=["localhost"])
    switcher={
        "1": elastic_client.search(
            index="kibana_sample_data_ecommerce",
            body= query1
               
        ),
        "2": elastic_client.search(
            index="kibana_sample_data_ecommerce",
            body= query2 

        ),
        "3": elastic_client.search(
            index="kibana_sample_data_ecommerce",
            body= query3
        ),
        "4": elastic_client.search(
            index="kibana_sample_data_ecommerce",
            body= query4  
            
        ),
        "5": elastic_client.search(
            index="kibana_sample_data_ecommerce",
            body= query5
        )
    }
    return switcher.get(query_index, None)

def setQueryOnTheEditor(query_index) :
    switcher={
        "1": query1,
        "2": query2,
        "3": query3,
        "4": query4,
        "5": query5
    }
    return switcher.get(query_index, None)

