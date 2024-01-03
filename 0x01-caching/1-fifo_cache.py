#!/usr/bin/python3
""" Caching Implementation.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ First In First Out Caching Class
    """

    def __init__(self):
        super().__init__()
        self.__queue = []

    def put(self, key, item):
        """ Put an item in the cache
        """
        if key and item:
            self.cache_data.update({key: item})
            self.__queue.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                first_in = self.__queue.pop(0)
                self.cache_data.pop(first_in)
                print(f'DISCARD: {first_in}')

    def get(self, key):
        """ Get an item from the cache
        """
        return self.cache_data.get(key, None)
