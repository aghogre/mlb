# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:24:05 2019

@author: Anshul
"""

from config import argument_config, mongo_config
from extractor import stl_batting_stats, json_object_building, a_team_batting_stats, minor_json_object_building
from mongoDBconnection import update_mongo_collection, initialize_mongo
import logging


def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s \
                        %(module)s.%(funcName)s :: %(message)s',
                        level=logging.INFO)
    source = mongo_config.get('col_name')
    mongo_colln = initialize_mongo(source)
    archive_url1 = argument_config.get('stl1_batting')
    archive_url2 = argument_config.get('stl2_batting')
    archive_url3 = argument_config.get('stl3_batting')
    archive_url10 = argument_config.get('stl11_batting')
    archive_url20 = argument_config.get('stl22_batting')
    archive_url30 = argument_config.get('stl33_batting')
    archive_url100 = argument_config.get('stl111_batting')
    archive_url200 = argument_config.get('stl222_batting')
    archive_url300 = argument_config.get('stl333_batting')
    a_team_list=[]
    l=[]
    peoria_chiefs_batting = argument_config.get('peoria_chiefs_batting')
    springfield_cardinals_batting = argument_config.get('springfield_cardinals_batting')
    memphis_redbirds_batting = argument_config.get('memphis_redbirds_batting')
    minor_url_list = [peoria_chiefs_batting, springfield_cardinals_batting, memphis_redbirds_batting]
    url_list = [archive_url1, archive_url2, archive_url3, archive_url10, archive_url20, archive_url30, archive_url100, archive_url200, archive_url300]
    try:
        var1 = 0
        var2 = 1
        var3 = 2
        logging.info("Starting Data Extraction for St Louis Cardinals Batters")
        for count in range(0,3):

            for i in url_list:
                
                stats_empty_list = []
                stat_list = stl_batting_stats(i, stats_empty_list)
                l = json_object_building(stat_list, i, url_list[var1], url_list[var2], url_list[var3])
                logging.info("Loading Data To Mongo")
                if not l:
                    continue
                else:
                    for obj in l:
                        mongo_id = obj["NAME"]+"-"+obj["TEAM"]
                        feed_object = obj
                        update_mongo_collection(mongo_colln, mongo_id, feed_object)
                    var1 = var1 + 3
                    var2 = var2 + 3
                    var3 = var3 + 3
         
        logging.info("Starting Data Extraction for St Louis Cardinals Minor League Batters")    
        for i in minor_url_list:
            if i == peoria_chiefs_batting:
                team = "PEORIA CHIEFS"
            elif i == springfield_cardinals_batting:
                team = "SPRINGFIELD CARDINALS"
            elif i == memphis_redbirds_batting:
                team == "MEMPHIS REDBIRDS"
            data_list = a_team_batting_stats(a_team_list, i) 
            l = minor_json_object_building(data_list, team)
            data_list= []
        logging.info("Loading Data To Mongo")   
        for obj in l:
            mongo_id = obj["NAME"]+"-"+obj["TEAM"]
            feed_object = obj
            update_mongo_collection(mongo_colln, mongo_id, feed_object)
    except:
        logging.error("Error Occurs while scraping and loading, raise exception to check exact error")
        pass

    
if __name__ == '__main__':
   main()

