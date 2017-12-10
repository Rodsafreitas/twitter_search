# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:22:10 2017

@author: Rods Freitas
"""

from elasticsearch import Elasticsearch

es = Elasticsearch()

index_elastic = 'twitter'
data='data'

arrayList = []

def getData(tipo):
	for item in tipo:
		elasticResult = es.search(index=index_elastic,doc_type=data,
			body={"query": {"match": {'tipo':item}}})		
		
		arrayList.append((item,elasticResult))

	return arrayList	

def getQuantidade(objeto):
	return objeto['hits']['total']
