# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    N = len(A)
    A_sorted = sorted(A)
    for i in range(N):
        if A_sorted[i] != i + 1:
            return 0
    return 1
