def intersection(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1

    return result


arr1 = [1, 2, 3, 4, 4, 5]
arr2 = [2, 3, 4, 4]

print("Intersection:", intersection(arr1, arr2))
