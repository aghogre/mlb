# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:39:02 2019

@author: Anshul
"""

import os

argument_config = {'stl1_batting': os.getenv('SLT1_BATTING','http://www.espn.com/mlb/stats/batting/_/league/nl/qualified/true'),
                   'stl2_batting': os.getenv('SLT2_BATTING','http://www.espn.com/mlb/stats/batting/_/league/nl/type/expanded'),
                   'stl3_batting': os.getenv('SLT3_BATTING','http://www.espn.com/mlb/stats/batting/_/league/nl/type/sabermetric'),
                   'stl11_batting': os.getenv('SLT11_BATTING','http://www.espn.com/mlb/stats/batting/_/league/nl/count/41/qualified/true'),
                   'stl22_batting': os.getenv('SL22_BATTING','http://www.espn.com/mlb/stats/batting/_/league/nl/count/41/qualified/true/type/expanded'),
                   'stl33_batting': os.getenv('SLT33_BATTING','http://www.espn.com/mlb/stats/batting/_/league/nl/count/41/qualified/true/type/sabermetric'),
                   'stl111_batting': os.getenv('SLT111_BATTING','http://www.espn.com/mlb/stats/batting/_/league/nl/count/81/qualified/true'),
                   'stl222_batting': os.getenv('SLT222_BATTING','http://www.espn.com/mlb/stats/batting/_/league/nl/count/81/qualified/true/type/expanded'),
                   'stl333_batting': os.getenv('SLT133_BATTING','http://www.espn.com/mlb/stats/batting/_/league/nl/count/81/qualified/true/type/sabermetric'),
                   'peoria_chiefs_batting': os.getenv('PEORIA_CHIEFS_BATTING','https://www.baseball-reference.com/register/team.cgi?id=1d3434c5'),
                   'springfield_cardinals_batting': os.getenv('SPRINGFIELD_CARDINALS_BATTING','https://www.baseball-reference.com/register/team.cgi?id=9abd2ddc'),
                   'memphis_redbirds_batting': os.getenv('MEMPHIS_REDBIRDS_BATTING','https://www.baseball-reference.com/register/team.cgi?id=499c0449')
                   
                   }
                  

mongo_config = {
    'mongo_uri': os.getenv('MONGO_URI', 'mongodb://admin:admin@mlbstats-shard-00-00-clx9y.mongodb.net:27017,mlbstats-shard-00-01-clx9y.mongodb.net:27017,mlbstats-shard-00-02-clx9y.mongodb.net:27017/test?ssl=true&replicaSet=MLBStats-shard-0&authSource=admin&retryWrites=true'),
    'db_name': os.getenv('MONGO_DB_NAME', 'mlb'),
    'col_name': os.getenv('MONGO_COL_NAME', 'batter'),
    #'mongo_index_name': os.getenv('MONGO_INDEX_NAME', 'csrtc'),
    #'ssl_required': os.getenv('MONGO_SSL_REQUIRED', False)
}