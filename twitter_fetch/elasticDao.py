# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 20:25:37 2017

@author: Rods Freitas
"""

from elasticsearch import Elasticsearch

#change url for python's container see elasticsearch's container
es = Elasticsearch(hosts=[{'host':'elasticsearch','port':9200}])

filtros = {'python','javascript','ux','css','html'}
index_elastic = 'twitter'
data = 'data'

#PUT data to elasticsearch
def SendAPI(tweet,tipo):
    if tipo != "":
        es.index(index=index_elastic,doc_type=data,
        body={"tweet": tweet, "tipo":tipo})    

#Mining data and type
def ExtractData(data):
    
    data = data.split(',')[3]
    tweet = data[8:len(data)]  
    #define type           
    tipo = ''      
    for i in filtros:
        if i in tweet:
            tipo = i
        
    return tweet, tipo        