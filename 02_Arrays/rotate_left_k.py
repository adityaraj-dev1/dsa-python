def rotate(arr, k):
    if len(arr) == 0:
        return arr

    n = len(arr)
    k = k % n

    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    reverse(0, k - 1)
    reverse(k, n - 1)
    reverse(0, n - 1)

    return arr


arr = [1, 2, 3, 4, 5, 6]
k = 2
print("Left rotated array:", rotate(arr, k))
