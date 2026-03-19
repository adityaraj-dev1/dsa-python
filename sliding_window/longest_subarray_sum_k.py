"""
Problem: Longest Subarray with Sum = K
Approach: Sliding Window
Condition: Works only for positive integers
Time Complexity: O(n)
Space Complexity: O(1)
"""

def longest_subarray(arr, k):
    i = 0
    curr_sum = 0
    maxi = 0

    for j in range(len(arr)):
        curr_sum += arr[j]

        while curr_sum > k:
            curr_sum -= arr[i]
            i += 1

        if curr_sum == k:
            maxi = max(maxi, j - i + 1)

    return maxi


arr = [1,2,2,4,3,2,1,1]
k = 4
print(longest_subarray(arr,k))
