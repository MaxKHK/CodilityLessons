#function checks if a sequence is a permutation
#of arithmetical progression

def solution(A):
    A.sort()
    for i in range(0, len(A)):
        if A[i] != i+1:
            return 0
        else:
            continue
    return 1
