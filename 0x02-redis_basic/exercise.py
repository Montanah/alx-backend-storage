#!/usr/bin/env python3
"""Creating a Cache class."""

import sys
import redis
from functools import wraps
from uuid import uuid4
from typing import Optional, Union, Callable


def count_calls(method: Callable) -> Callable:
    """Count the number of times a method is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs for a particular function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes,
                                                                    int, float,
                                                                    None]:
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


def replay(method: Callable):
    """Display the history of calls of a particular function"""
    r = redis.Redis()
    name = method.__qualname__
    count = r.get(name).decode('utf-8')
    inputs = r.lrange(name + ":inputs", 0, -1)
    outputs = r.lrange(name + ":outputs", 0, -1)

    print("{} was called {} times:".format(name, count))

    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))
    return method
