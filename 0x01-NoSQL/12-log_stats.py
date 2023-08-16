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
    logs = client.logs.nginx

    # Access the database and collection
    database_name = 'logs'
    collection_name = 'nginx'
    db = client[database_name]
    collection = db[collection_name]
        
    # Total number of logs
    total_logs = logs.count_documents({})
    print("{} logs".format(total_logs))
    
    # Methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = logs.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))
    
    # Number of documents with method=GET and path=/status
    status_check_count = logs.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check_count))

