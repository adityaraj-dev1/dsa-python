from collections import deque

def first_negative(arr, k):
    i = 0
    q = deque()
    result = []

    for j in range(len(arr)):

        if arr[j] < 0:
            q.append(j)  

        if j - i + 1 == k:

            if q:
                result.append(arr[q[0]])
            else:
                result.append(0)

    
            if q and q[0] == i:
                q.popleft()

            i += 1

    return result


arr = [-1, 2, -3, 4, -7, 5, 6, -8]
k = 3
print(first_negative(arr, k))
