#!/usr/bin/env python3
"""Creating a Cache class."""

import redis
from functools import wraps
from uuid import uuid4
from typing import Optional, Union, Callable


def count_calls(method: Callable) -> Callable:
    """
    decorator that takes a single method Callable argument and returns a
    Callable
    """
    @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            """
            function that increments the count for that key every time the
            method is called and returns the value returned by the original
            method.
            """
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)

        return wrapper


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

    def get(self, key: str, fn: Optional[Callable] = None)-> Union[str, bytes,
    int, float, None]:
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
        return self.get(key, int)

    def get_str(self: bytes) -> str:
        """getting a string"""
        return self.get(key, lambda x: x.decode("utf-8"))
