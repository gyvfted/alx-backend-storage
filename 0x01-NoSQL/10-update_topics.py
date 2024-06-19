#!/usr/bin/env python3
"""
Change school topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update document with a specific attr: value
    """
    return mongo_collection.update_many({
            "name": name
        },
        {
            "$set": {
                "topics": topics
            }
        })
