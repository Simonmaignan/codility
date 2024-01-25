# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Implement your solution here
    M = len(A)
    max_counter = 0
    counters = [0] * N
    for i in range(M):
        if A[i] == N + 1:
            counters = [max_counter] * N
        else:
            counters[A[i] - 1] += 1
            max_counter = max(max_counter, counters[A[i] - 1])

    return counters