arr = [4, 7, 2, 9, 1, 8]

largest = None
second = None
third = None

for x in arr:
    if largest is None or x > largest:
        third = second
        second = largest
        largest = x
    elif x != largest and (second is None or x > second):
        third = second
        second = x
    elif x != largest and x != second and (third is None or x > third):
        third = x

print("Third largest element:", third)
