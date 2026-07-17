arr = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(arr)):
    complement = target - arr[i]
    if complement in seen:
        print("Indices:", seen[complement], i)
        break
    seen[arr[i]] = i
