#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://localhost:27017')
    logs_collection = client.logs.nginx
    number_of_documents = logs_collection.count_documents({})
    print("{} logs".format(number_of_documents))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        number_of_methods = logs_collection.count_documents(
            {"method": method})
        print("\tmethod {}: {}".format(method, number_of_methods))
    number_of_status = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(number_of_status))
