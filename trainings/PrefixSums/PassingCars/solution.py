# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from typing import List


def solution(a: List[int]):
    # Implement your solution here
    n = len(a)
    east_traveling_cars = [0] * (n + 1)
    passing_cars = [0] * (n + 1)
    for k in range(0, n):
        east_traveling_cars[k + 1] = east_traveling_cars[k] + 1 - a[k]
        passing_cars[k + 1] = passing_cars[k] + a[k] * east_traveling_cars[k]

    if passing_cars[-1] > 1e9:
        return -1

    return passing_cars[-1]
