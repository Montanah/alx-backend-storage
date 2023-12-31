#!/usr/bin/env python3
""" Lists all documents in Python """

import pymongo


def list_all(mongo_collection):
    """ lists all documents in a collection """
    if not mongo_collection:
        return []
    return mongo_collection.find()
