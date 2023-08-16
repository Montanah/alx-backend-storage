#!/usr/bin/env python3
"""Creating a Cache class."""

import redis
import uuid
from typing import Union


class Cache:
    """Cache class"""

    def __init__(self):
        """Method constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """Method that generates a random key"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
