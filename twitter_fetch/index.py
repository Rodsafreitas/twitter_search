# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 20:22:23 2017

@author: Rods Freitas
"""

#imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import elasticDao

#authentications
client_key = "Mf2dbZhhfvKrp1wQLcPI3O9T3"
client_secret = "SPOROqMhSFqEPWvgy26kFWJcq4qqF0hHiJMSnOsKZvq5furWjQ"
token = "1891363410-hjfn0N5tWtl9XdBMQ8pFSASWesUfosysWMLQTl1"
token_secret = "wMBRZmabKP4LdSTQNeTaLCEonPc0H9RVlzCzlZzxeREx3"

#filters        
filtro = {'python','javascript','ux','html'}

class listener(StreamListener):

    def on_data(self, data):                
        
        #call correct def
        tweet,tipo = elasticDao.ExtractData(data)         
        #send data elasticsearch
        elasticDao.SendAPI(tweet,tipo)   

        return True

    def on_error(self, status):
        print(status)
       
if __name__ == '__main__':    
    #authenticate
    auth = OAuthHandler(client_key, client_secret)
    auth.set_access_token(token, token_secret)
    twitterStream = Stream(auth=auth, listener=listener())
    #set filter to search
    twitterStream.filter(track=filtro)
 