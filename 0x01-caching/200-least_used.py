#!/usr/bin/python3
""" Caching Implementation.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Least Recently Used Caching Class
    """

    def __init__(self):
        super().__init__()
        self.__trackpad = {}

    def put(self, key, item):
        """ Put an item in the cache
        """
        if key and item:
            self.cache_data.update({key: item})
            if len(self.cache_data) > self.MAX_ITEMS:
                least_used = min(self.__trackpad, key=lambda k: self.__trackpad[k])
                self.cache_data.pop(least_used)
                print(f'DISCARD: {least_used}')

    def get(self, key):
        """ Get an item from the cache
        """
        count = self.__trackpad.get(key, None)
        if count:
            count += 1
            self.__trackpad.update({key: count})
        else:
            self.__trackpad.update({key: 1})
        return self.cache_data.get(key, None)
