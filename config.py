# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:39:02 2019

@author: Anshul
"""

import os

argument_config = {'stl_batting': os.getenv('STL_BATTING', 'https://www.baseball-reference.com/teams/STL/2019.shtml'),
                   'peoria_chiefs_batting': os.getenv('PEORIA_CHIEFS_BATTING','https://www.baseball-reference.com/register/team.cgi?id=1d3434c5'),
                   'springfield_cardinals_batting': os.getenv('SPRINGFIELD_CARDINALS_BATTING','https://www.baseball-reference.com/register/team.cgi?id=9abd2ddc'),
                   'memphis_redbirds_batting': os.getenv('MEMPHIS_REDBIRDS_BATTING','https://www.baseball-reference.com/register/team.cgi?id=499c0449')
                   
                   }
                  

mongo_config = {
    #'mongo_uri': os.getenv('MONGO_URI', 'mongodb://admin:admin@mlbstats-shard-00-00-clx9y.mongodb.net:27017,mlbstats-shard-00-01-clx9y.mongodb.net:27017,mlbstats-shard-00-02-clx9y.mongodb.net:27017/test?ssl=true&replicaSet=MLBStats-shard-0&authSource=admin&retryWrites=true'),
    'mongo_uri': os.getenv('MONGO_URI', 'mlbstats-shard-00-01-clx9y.mongodb.net:27017'),
    'db_name': os.getenv('MONGO_DB_NAME', 'mlb'),
    'col_name': os.getenv('MONGO_COL_NAME', 'batter'),
    'requires_auth': os.getenv('REQUIRES_AUTH', 'true'),
    'mongo_username': os.getenv('MONGO_USER', 'admin'),
    'mongo_password': os.getenv('MONGO_PASSWORD', 'admin'),
    'mongo_auth_source': os.getenv('MONGO_AUTH_SOURCE', 'admin'),
    'mongo_auth_mechanism': os.getenv('MONGO_AUTH_MECHANISM', 'SCRAM-SHA-1'),
    #'mongo_index_name': os.getenv('MONGO_INDEX_NAME', 'csrtc'),
    'ssl_required': os.getenv('MONGO_SSL_REQUIRED', True)
}