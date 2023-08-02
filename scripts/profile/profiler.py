"""Module py-web-service"""

import os
import sys

sys.path.append("/opt/dev")

import time
import random

from core.common import find_top_n_elements_from_list_minheap
from core.common import find_top_n_elements_from_list_heapq
from core.common import find_top_n_elements_from_list_sort

from memory_profiler import profile

from argparse import ArgumentParser


@profile
def _function(f, *args, **kwargs):
    return f(*args, **kwargs)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-l", "--list_size", dest="list_size", help="The size of num_list", metavar="NUM_LIST", default=10000, type=int)
    parser.add_argument("-t", "--top_n", dest="top_n", help="top_n", metavar="TOP_N", default=1000, type=int)
    parser.add_argument("-r", "--iteration", dest="iteration", help="Iteration", metavar="ITERATION", default=10, type=int)
    args = parser.parse_args()

    num_list = [random.randint(-100000, 10000000) for _ in range(args.list_size)]
    top_n = args.top_n

    funcs = {
        "sort": find_top_n_elements_from_list_sort,
        "heapq": find_top_n_elements_from_list_heapq,
        "minheap": find_top_n_elements_from_list_minheap,
    }

    print("---------Memory Profiling---------")
    print("Size of num_list:", args.list_size)
    print("Top n:", args.top_n)
    print()
    print(f"Test case: the size of num_list: {len(num_list)} and top_n: {top_n}")
    for f in funcs:
        print("Memory usage for", f)
        _function(funcs[f], num_list, top_n)
    print("----------------------------------")
    print()


    print("------Execute Time Profiling------")
    print("Size of num_list:", args.list_size)
    print("Top n:", args.top_n)
    print("Iteration:", args.iteration)
    print()
    total_times = {
        "sort": 0,
        "heapq": 0,
        "minheap": 0,
    }

    iteration = args.iteration
    for _ in range(iteration):
        num_list = [random.randint(-100000, 10000000) for _ in range(1000000)]
        top_n = random.randint(100, 20000)

        for f in funcs:
            start_time = time.time()
            funcs[f](num_list, top_n)
            total_times[f] += time.time() - start_time

    print("Average times:")
    for f in funcs:
        print("Total average times for", f, total_times[f]/iteration)
    print("----------------------------------")
    print()
