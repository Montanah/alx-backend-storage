#!/usr/bin/env python3
"""Creating a Cache class."""

import sys
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


 @functools.lru_cache(maxsize=None)
    def store(self, data):
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def call_history(method: Callable) -> Callable:
        """appending the input arguments"""
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            input_key = f"{method.__qualname__}:inputs"
            output_key = f"{method.__qualname__}:outputs"
            
            # Store input arguments as a normalized string
            input_data = str(args)
            self._redis.rpush(input_key, input_data)
            
            # Execute the wrapped function to retrieve the output
            output = method(self, *args, **kwargs)
            
            # Store the output in the Redis list
            self._redis.rpush(output_key, output)
            
            return output

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
