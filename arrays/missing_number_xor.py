def missing_number(arr, n):
    xor1 = 0
    xor2 = 0

    for i in range(1, n + 1):
        xor1 ^= i

    for num in arr:
        xor2 ^= num

    return xor1 ^ xor2


arr = [1, 2, 4, 5]
n = 5

print("Missing number:", missing_number(arr, n))
