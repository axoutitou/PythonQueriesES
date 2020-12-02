
# Work by Florin-Alexandru POSCHINA & Axel CARNEZ

## Lab 1 : Elasticsearch & Kibana discovery

### Install Elasticsearch 

Download from : 
>https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html#run-elasticsearch-local

Extract : in C:\WorkspaceBD

To personnalize our elasticsearch cluster edit : elasticsearch-7.10.0\config\elasticsearch.yml (Uncomment the line cluster.name

Tu run it :
	- Go to : elasticsearch-7.10.0\bin
	- Execute : .\elasticsearch.bat
You can access it from : http://localhost:9200/

![Get-Image-1](https://i.ibb.co/r6fBGqs/1.png)

### Install Kibana

Download from : 
>https://www.elastic.co/guide/en/kibana/current/windows.html#install-windows

Extract : in C:\WorkspaceBD

To run it :
	- Go to : kibana-7.10.0-windows-x86_64\bin
	- Execute : .\kibana.bat
	- You can access it from : http://localhost:5601/

![Get-Image-1](https://i.ibb.co/JpZ4TD0/2.png)

### Load some sample data to discover Kibana

Following the tutorial : https://www.elastic.co/guide/en/kibana/7.9/tutorial-sample-data.html

- 1.1 Please select some filters on the [Flights] Global Flight Dashboard, based on your favorite destinations and do a screenshot of it that you will add in your report. 


![Get-Image-1](https://i.ibb.co/rHH91n0/3.png)

### Load your first data into ES and visualize it

Download the data :

>curl -O https://download.elastic.co/demos/kibana/gettingstarted/8.x/shakespeare.json
>curl -O https://download.elastic.co/demos/kibana/gettingstarted/8.x/accounts.zip
>curl -O https://download.elastic.co/demos/kibana/gettingstarted/8.x/logs.jsonl.gz

Create the index :

>PUT /shakespeare
>{
>  "mappings": {
>    "properties": {
>    "speaker": {"type": "keyword"},
>    "play_name": {"type": "keyword"},
>    "line_id": {"type": "integer"},
>    "speech_number": {"type": "integer"}
>    }
>  }
>}

>PUT /logstash-2015.05.18
>{
>  "mappings": {
>    "properties": {
>      "geo": {
>        "properties": {
>          "coordinates": {
>            "type": "geo_point"
>          }
>        }
>      }
>    }
>  }
>}

>PUT /logstash-2015.05.19
>{
>  "mappings": {
>    "properties": {
>      "geo": {
>        "properties": {
>          "coordinates": {
>            "type": "geo_point"
>          }
>        }
>      }
>    }
>  }
>}

>PUT /logstash-2015.05.20
>{
>  "mappings": {
>    "properties": {
>      "geo": {
>        "properties": {
>          "coordinates": {
>            "type": "geo_point"
>          }
>        }
>      }
>    }
>  }
>}

If you need to delete an index :

>DELETE logstash*

Load the data (in PowerShell) :

>Invoke-RestMethod "http://localhost:9200/bank/account/_bulk?pretty" -Method Post -ContentType 'application/x-ndjson' -InFile "accounts.json"
>Invoke-RestMethod "http://localhost:9200/shakespeare/_bulk?pretty" -Method Post -ContentType 'application/x-ndjson' -InFile "shakespeare.json"
>Invoke-RestMethod "http://localhost:9200/_bulk?pretty" -Method Post -ContentType 'application/x-ndjson' -InFile "logs.jsonl"

Create index :
>https://www.elastic.co/guide/en/kibana/7.9/tutorial-define-index.html#_create_an_index_pattern_for_the_time_series_data

Discover the data :
>https://www.elastic.co/guide/en/kibana/7.9/tutorial-discovering.html

- 1.1 Please specify in your report the total number of documents of each index.

![Get-Image-1](https://i.ibb.co/ySYyNyK/4.png)

- 1.2 Please do some screenshots of at least 1 search or filter you applied on each index

![Get-Image-1](https://i.ibb.co/crwDk2x/5.png)
![Get-Image-1](https://i.ibb.co/gDQspqM/6.png)
![Get-Image-1](https://i.ibb.co/XSHBm0n/7.png)

Create visualization :
>https://www.elastic.co/guide/en/kibana/7.9/tutorial-visualizing.html

Create dashboard :
>https://www.elastic.co/guide/en/kibana/7.9/tutorial-dashboard.html

- 1.3 Do a screenshot of the dashboard and add it to your report

![Get-Image-1](https://i.ibb.co/16y9c1T/8.png)

## Lab 2 : Scale Elasticsearch with shards & nodes

- 2.1 Do a screenshot of the monitoring and add it to your report

![Get-Image-1](https://i.ibb.co/x7bHpB1/9.png)

- What is their status ? Do they have unassigned shards ?
Every indice are in the state "Yellow". They also all have one unassigned shards.

- 2.2 Do a screenshot of indices monitoring and add it to your report

![Get-Image-1](https://i.ibb.co/kxD3QXK/10.png)

Meaning of status color in “Indices” monitoring : 
	• Green : all shards of the index assigned 
	• Yellow : some replicas shards of the index not assigned 
	• Red : some primary shards of the index not assigned (some data are not available) 

- Why is there unassigned shards for all our indices created in Lab 1 ?
Maybe its just because we only have one node. We d'ont have any interest to replic our shard on the same node

2.3 Do a screenshot of the monitoring of the “bank” index and add it to your report

![Get-Image-1](https://i.ibb.co/njQHrYX/11.png)

Problem of free space on my computer -> Impossible to enable replica.
Solve the problem by editing "elasticsearch.yaml" and adding :

>cluster.routing.allocation.disk.watermark.low: 1gb
>cluster.routing.allocation.disk.watermark.high: 1gb
>cluster.routing.allocation.disk.watermark.flood_stage: 1gb

- 2.4 Do a screenshot of the monitoring of the “bank” index, after the addition of 1 node and add it to your report. Comment about what happen on the bank index monitoring page ?

![Get-Image-1](https://i.ibb.co/BsNTLpL/12.png)

Our replica shard as now been assigned to a node (node2 more precisely)

- 2.5 Do a screenshot of the monitoring of the “bank” index, after the addition of 2 nodes and add it to your report. Comment about what happen on the bank index monitoring page ? 

![Get-Image-1](https://i.ibb.co/GHLyDPJ/13.png)

Nothing change cause we only have define 1 primay shard and 1 replica shard. My two shard are already assign so it's good

However my three nodes are well visible by kibana :

![Get-Image-1](https://i.ibb.co/rxGRDPm/14.png)

- 2.6 Do a screenshot of indices monitoring, after the addition of 2 nodes and add it to your report

![Get-Image-1](https://i.ibb.co/zN2YWGh/15.png)

Every indice is in the "Green" states et every shards are assigned.

- 2.7 Do a screenshot of the monitoring of the “bank” index, after reducing number of replica to 0 and add it to your report. What happened ?

![Get-Image-1](https://i.ibb.co/Pcr8yVd/16.png)

There is no more replica shard for my index bank

- 2.8 Do a screenshot of the monitoring of the “bank” index, after increasing number of replica to 2 and add it to your report. What happened ? 

![Get-Image-1](https://i.ibb.co/VmrzfD2/17.png)

I have two replica shard for my index bank. The primary shard is on node1 and the replica shards are on node2 and node3.

## Lab 3 : Start playing with search & aggregation queries

- 3.1 Do a screenshot of your search results and add it to your report

![Get-Image-1](https://i.ibb.co/bzx8sMZ/18.png)

- Add the exact number of hits in your report that you will get from this request.
We have 32484 document who are matching this sentence

![Get-Image-1](https://i.ibb.co/7pWxdyj/19.png)

- 3.2 Do a screenshot of your search profiler and add it to your report 

![Get-Image-1](https://i.ibb.co/nMWMRxZ/20.png)

- 3.3 Do a screenshot of the result of this command

![Get-Image-1](https://i.ibb.co/xM2Mhn6/21.png)

- 3.4 Do a screenshot of this search query results and add it to your report

![Get-Image-1](https://i.ibb.co/QKFDZj8/22.png)

- 3.5 Do copy / paste all the queries you wrote in Dev Tools during this lab and add it to your report

>PUT /shakespeare/_settings
>{
> "settings": {
>  "index.blocks.write": true
> }
>}
>
>POST shakespeare/_split/shakespeare-catalog
>{
> "settings": {
>  "index.number_of_shards": 2
> }
>}
>
>DELETE shakespeare
>
>GET /shakespeare-catalog/_search
>{
> "query": {
>   "match": {
>    "text_entry": "The edge of war"
>   }
> }
>}
>
>GET /shakespeare-catalog/_search
>{
> "track_total_hits": true,
>   "query": {
>     "match": {
>      "text_entry": "The edge of war"
>   }
> }
>}
>
>GET /shakespeare-catalog/_search
>{
>   "query": {
>     "match": {
>       "text_entry": {
>         "query": "The edge of war",
>         "operator": "AND"
>     }
>   }
> }
>}
>
>GET /shakespeare-catalog/_search
>{
> "query": {
>   "match": {
>     "text_entry": {
>       "query": "The edge of war",
>       "minimum_should_match": "2"
>     }
>   }
> }
>}
>
>GET /shakespeare-catalog/_search
>{
> "query": {
>   "match": {
>     "text_entry": {
>       "query": "The edge of war",
>       "minimum_should_match": "2"
>     }
>   }
> },
> "sort": [
>   {
>     "_score": {
>     "order": "asc"
>     }
>   }
> ]
>}
>
>PUT /shakespeare-catalog-2
>{
> "mappings": {
>   "properties": {
>     "speaker": {
>      "type": "keyword"
>     },
>     "play_name": {
>      "type": "keyword"
>     },
>     "line_id": {
>      "type": "integer"
>     },
>     "speech_number": {
>      "type": "integer"
>     },
>    "text_entry": {
>       "type": "text",
>        "fields": {
>          "english": {
>           "type": "text",
>            "analyzer": "english"
>          }
>        }
>      }
>   }
> }
>}
>
>POST _reindex
>{
> "source": {
>  "index": "shakespeare-catalog"
> },
> "dest": {
>  "index": "shakespeare-catalog-2",
>  "version_type": "internal"
> }
>}
>
>GET /_cat/indices/
>
>GET /shakespeare-catalog-2/_search
>{
> "query": {
>   "match": {
>     "text_entry.english": {
>      "query": "The edge of war",
>      "minimum_should_match": "2"
>     }
>   }
> },
> "sort": [
>   {
>     "_score": {
>      "order": "asc"
>     }
>  }
> ]
>}
>
>GET /_analyze/
>{
> "analyzer": "default",
> "text":"The edge of war"
>}
> 
>GET /_analyze/
>{
> "analyzer": "english",
> "text":"The edge of war"
>}
>
>GET /shakespeare-catalog-2/_search
>{
> "query": {
>   "match": {
>     "text_entry.english": {
>      "query": "The edge of war"
>     }
>   }
> },
> "sort": [
>   {
>     "_score": {
>      "order": "asc"
>     }
>   }
> ]
>}
>
>GET /shakespeare-catalog-2/_search
>{
> "query": {
>   "match": {
>      "text_entry.english": {
>        "query": "The edge of war"
>     }
>   }
> },
> "size": 20
>}

- 3.6 Do a screenshot of your aggregation query results and add it to your report

![Get-Image-1](https://i.ibb.co/586ZpmL/23.png)

- 3.7 Do a screenshot of your search & aggregation query results and add it to your report

![Get-Image-1](https://i.ibb.co/X2w4B8T/24.png)
![Get-Image-1](https://i.ibb.co/TgQGjHY/25.png)

- 3.8 Do a screenshot of the response in the inspect panel and add it to your report

![Get-Image-1](https://i.ibb.co/5FZL2zx/26.png)

- 3.9 Do a screenshot of the response in the inspect panel and add it to your report

![Get-Image-1](https://i.ibb.co/BcFGNWP/27.png)

- 3.10 Do a screenshot of the response in the inspect panel and add it to your report

![Get-Image-1](https://i.ibb.co/svwN1sq/28.png)

- 3.11 Do a screenshot of the visualization and settings and add it to your report 

![Get-Image-1](https://i.ibb.co/m0VrTtD/29.png)

- 3.12 Do a screenshot of the dashboard and add it to your report 

![Get-Image-1](https://i.ibb.co/Sx0XjqF/30.png)

## Lab 4 :

For this lab we have develop a web interface that allow user to run his own queries on ElasticSearch
This application is running on flask with python. In order to make it run on your machine youd need to install :
>pip instal elasticsearch
>pip instal Flask

You also need to have an elastcisearch running localy on your machine with the following example dataset :

![Get-Image-1](https://i.ibb.co/z24p0jd/31.png)

You can then run the application with the command :
>python app.py

The application is accesible at :
- Windows : 127.0.0.1:5000
- Linux : 0.0.0.0:5000

### Screenshot of the user interface
![Get-Image-1](https://i.ibb.co/qyvX9Nx/1.png)
- 1. The user can search for a precise field he wants to build a query on
- 2. The user has an overview of the entire index mapping dataset (or just of the searched fields) in order to help him build the query
- 3. The user can access some already written queries as example by dropping the list. The querry will be shown in the  field and the result in the field 5.
- 4. The user can enter a query to be executed in the field 4. The query selected from the examples will also be shown here.
- 5. The response as it is received from the Kibana server will be displayed here

### Working example

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

### Non working example

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
>(Because of the ',' symbol)

Here we have trouble with queries that contain , or []. In fact we have to turn string expresion, wrote by the user in our textearea into a python nested dictionnary. We didn't found library to do this convertion so we have implemented our own parser in order to realise it. We can improve the autorised queries by improving our parser. However we didn't have enough time to do it.