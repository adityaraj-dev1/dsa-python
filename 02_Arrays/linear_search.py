arr = [3, 5, 7, 9, 2]
target = 7
found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index:", i)
        found = True
        break

if not found:
    print("Not found")
