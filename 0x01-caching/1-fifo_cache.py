#!/usr/bin/python3
""" Caching Implementation.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ First In First Out Caching Class
    """

    def put(self, key, item):
        """ Put an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        return self.cache_data.get(key, None)
