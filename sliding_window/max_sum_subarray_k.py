def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None

    i = 0
    window_sum = 0
    max_sum = float('-inf')

    for j in range(n):
        window_sum += arr[j]

        if j - i + 1 == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i]
            i += 1

    return max_sum


arr = [1, 3, 4, 5, 2, 5]
k = 3
print("Maximum sum:", max_sum_subarray(arr, k))
