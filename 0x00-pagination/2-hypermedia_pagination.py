#!/usr/bin/env python3
'''
    Pagination
'''
import csv
import math
from typing import List, Tuple, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        '''
             return a tuple of size two containing a
             start index and an end index corresponding to the
             range of indexes to return in a list
             for those particular pagination parameters.
        '''
        end_index = page * page_size
        return (end_index - page_size, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
            Paginates dataset
        '''
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start, end = self.index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10
                  ) -> Dict[str, Union[int, List[List], None]]:
        '''
            Gets Hypermedia
        '''
        dataset = self.get_page(page, page_size)
        rows = len(self.dataset())
        total_pages = int(rows / page_size)
        return {
                'page_size': len(dataset),
                'page': page,
                'data': dataset,
                'next_page': page + 1 if page < total_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
                }
