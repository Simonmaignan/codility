# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from typing import List


def solution(a: List[int]):
    # Implement your solution here
    k_max = 1000000
    counter = [0] * (k_max)
    for k in a:
        if k > 0:
            counter[k - 1] += 1

    for k in range(k_max - 1):
        if counter[k] == 0:
            return k + 1
