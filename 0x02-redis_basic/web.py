#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""

import redis
import requests
from typing import Callable
from functools import wraps


def count_requests(method: Callable) -> Callable:
    """Count the number of times a request has been made"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(url):
        """Wrapper function"""
        self._redis.incr(key)
        return method(url)

    return wrapper


class Cache:
    """Cache class"""
    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_requests
    def get_page(self, url: str) -> str:
        """Get the HTML content of a particular URL and return it"""
        response = requests.get(url)
        self._redis.setex(url, 10, response.text)
        return response.text
