#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stat():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://localhost:27017')
    logs = client.logs.nginx
    
    total_logs = logs.count_documents({})
    print(f"Total logs: {total_logs}")
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = logs.count_documents({"method": method})
        print(f"\tMethod {method}: {method_count}")
    
    status_check_count = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"Status check logs: {status_check_count}")


if __name__ == "__main__":
    log_stat()

