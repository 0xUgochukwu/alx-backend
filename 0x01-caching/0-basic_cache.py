#!/usr/bin/env python3
""" Caching
"""

BaseCaching = __import__('base-caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic Caching Class
    """

    def put(self, key, item):
        """ Put an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        return self.cache_data.get(key, None)
