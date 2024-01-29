# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A: int, B: int, K: int) -> int:
    # Implement your solution here

    sum_div_K = len(range(A, B, K))
    if K > (B - A):
        sum_div_K = 0
    if A == 0:
        sum_div_K += 1
    return sum_div_K
