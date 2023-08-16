#!/usr/bin/env python3
"""
Improve 12-log_stats.py by adding the top 10 of the most present IPs
in the collection nginx of the database logs
"""

from pymongo import MongoClient

if __name__ == "__main__":
    """
    adding the top 10 of the most present IPs in the collection nginx of
    the database logs
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

    # Top 10 of the most present IPs in the collection nginx
    top_ips = logs.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    print("IPs:")
    for ip in top_ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))
        

