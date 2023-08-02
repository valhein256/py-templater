"""
Module py-web-service Models

Find top n elements in a list

Parameters
----------
num_list : List[int]
    input list
n : int
    number of top elements to find

Returns
-------
List[int]
    top n elements in a list
"""

import heapq

from typing import List


def find_top_n_elements_from_list_base(num_list: List[int], top_n: int) -> List[int]:
    num_dict = {}
    for num in num_list:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    top_n_elements = []
    while len(top_n_elements) < top_n:
        max_num = max(num_dict)
        count = num_dict[max_num] if len(top_n_elements) + num_dict[max_num] <= top_n else top_n - len(top_n_elements)
        top_n_elements += [max_num] * count
        del num_dict[max_num]

    return top_n_elements


def find_top_n_elements_from_list_minheap(num_list: List[int], top_n: int) -> List[int]:

    if top_n <= 0:
        return []

    minheap = []
    for num in num_list:
        if len(minheap) < top_n:
            heapq.heappush(minheap, num)
        else:
            if num > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, num)

    return [heapq.heappop(minheap) for _ in range(len(minheap))][::-1]


def find_top_n_elements_from_list_heapq(num_list: List[int], top_n: int) -> List[int]:
    return heapq.nlargest(top_n, num_list)


def find_top_n_elements_from_list_sort(num_list: List[int], top_n: int) -> List[int]:
    return sorted(num_list, reverse=True)[:top_n]
