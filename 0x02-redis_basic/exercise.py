#!/usr/bin/env python3
"""Creating a Cache class."""

import sys
import redis
from uuid import uuid4
from typing import Union, Callable


class Cache:
    """Cache class"""

    def __init__(self):
        """Method constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method that generates a random key"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union
    [str, bytes, int, float, None]:
        """
        method that take a key string argument and an optional Callable
        argument named fn
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is None:
            return data
        return fn(data)

    def get_int(self: bytes) -> int:
        """getting a number"""
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """getingt a string"""
        return self.decode("utf-8")
