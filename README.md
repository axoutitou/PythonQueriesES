# PythonQueriesES

## Work by Florin-Alexandru POSCHINA & Axel Carnez

Example query :

## Working example
>query:{
>    match:{
>        customer_full_name:Tariq Rivera
>    }
>}

>"query":{
>    "match":{
>        "customer_full_name":"Tariq Rivera"
>    }
>}

>"aggs": {
>    "manufacturer": {
>      "terms": {
>        "field": "manufacturer.keyword"
>      }
>    }
>}

## Non working example

>"query": {
>    "match": {
>      "customer_gender": "MALE"
>    }
>  }
>  , "aggs": {
>    "manufacturer": {
>      "terms": {
>        "field": "manufacturer.keyword",
>        "size": 10
>      }
>    }
>  }
>
>(Because of the ,)