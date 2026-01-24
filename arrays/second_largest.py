arr = [10, 5, 20, 8]

largest = arr[0]
second_largest = -1

for x in arr:
    if x > largest:
        second_largest = largest
        largest = x
    elif x != largest and x > second_largest:
        second_largest = x

print("Second largest element:", second_largest)
