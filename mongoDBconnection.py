# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:38:47 2019

@author: Anshul
"""

from uuid import uuid1
from pymongo import MongoClient
import logging
from config import mongo_config


def make_mongo_connection(collection_name):
    """This is to establish connection with MongoDB with desired Credentials"""

    # Fetching config parameters.
    mongo_uri = mongo_config.get('mongo_uri')
    requires_auth = mongo_config.get('requires_auth')
    mongo_username = mongo_config.get('mongo_username')
    mongo_password = mongo_config.get('mongo_password')
    mongo_auth_source = mongo_config.get('mongo_auth_source')
    mongo_auth_mechanism = mongo_config.get('mongo_auth_mechanism')
    db_name = mongo_config.get('db_name')
    ssl_required = mongo_config.get('ssl_required')
    
    client = MongoClient(mongo_uri, username=mongo_username, password=mongo_password, authsource= mongo_auth_source,
                         authmechanism=mongo_auth_mechanism, ssl=ssl_required, replicaSet='MLBStats-shard-0')
    #client = pymongo.MongoClient(mongo_uri)
    """if requires_auth == 'true':
        client.the_database.authenticate(mongo_username,
                                         mongo_password,
                                         source=mongo_auth_source,
                                         mechanism=mongo_auth_mechanism
                                         )"""
       
    db = client[db_name]
    mongo_colln = db[collection_name]
    
    #client = pymongo.MongoClient("mongodb://admin:<password>@mlbstats-shard-00-00-clx9y.mongodb.net:27017,mlbstats-shard-00-01-clx9y.mongodb.net:27017,mlbstats-shard-00-02-clx9y.mongodb.net:27017/test?ssl=true&replicaSet=MLBStats-shard-0&authSource=admin&retryWrites=true")
    


    # Testing Index with Unique element, to avoid failure of Index creation,
    # in case of Collection doesnot exist.
    test_uuid = str(uuid1())
    try:
        mongo_colln.insert_one({'uuid': test_uuid})
        mongo_colln.delete_one({'uuid': test_uuid})
    except:
        logging.debug("Collection %s already exists" % collection_name)

    return mongo_colln


def initialize_mongo(source):
    """Initializes MongoDB Connection
    and returns MongoCollection with the given Index."""

    #mongo_index_name = mongo_config.get('mongo_index_name')
    #source = mongo_config.get('col_name')

    try:
        # Creating Mongo Collection
        mongo_colln = make_mongo_connection(source)

        # Create index, if it is not available.
        #if mongo_index_name not in mongo_colln.index_information():
        #mongo_colln.create_index(mongo_index_name, unique=False)

    except IOError:
        logging.error("Could not connect to Mongo Server")

    return mongo_colln


def insert_into_mongo(mongo_colln, feed_object):
    """To insert given JSON data into MongoDB."""
    try:
        mongo_colln.insert_one(feed_object)
    except:
        raise
        logging.error("Mongo Insert Exception.")
    finally:
        feed_object.clear
    return True


def update_mongo_collection(mongo_colln, mongo_id, feed_object):
    """To update existing JSON data into MongoDB."""
    try:
        
        mongo_colln.update_one({'_id': mongo_id}, {"$set": feed_object},
                               upsert=True)
    except:
        raise
        logging.error("Mongo Update Exception.")
    finally:
        feed_object.clear