#!/usr/bin/env python3
'''
    Pagination
'''


def index_range(page, page_size):
    '''
         return a tuple of size two containing a
         start index and an end index corresponding to the
         range of indexes to return in a list
         for those particular pagination parameters.
    '''
    end_index = page * page_size
    return (end_index - page_size, end_index)