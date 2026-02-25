from collections import deque

def max_of_every_window(arr, k):
    dq = deque()
    result = []
    i = 0

    for j in range(len(arr)):

        while dq and arr[j] >= arr[dq[-1]]:
            dq.pop()

        dq.append(j)

        if j - i + 1 == k:

            result.append(arr[dq[0]])
          
            if dq[0] == i:
                dq.popleft()

            i += 1

    return result


arr = [12, -23, 34, -23, 76, 89]
k = 3
print("Maximum in windows:", max_of_every_window(arr, k))
