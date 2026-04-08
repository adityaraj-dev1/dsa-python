def longest_substring_k_distinct(s, k):
    if len(s) < k:
        return 0

    i = 0
    freq = {}
    max_len = 0

    for j in range(len(s)):
        freq[s[j]] = freq.get(s[j], 0) + 1

        while len(freq) > k:
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                del freq[s[i]]
            i += 1

        if len(freq) == k:
            max_len = max(max_len, j - i + 1)

    return max_len


s = "aabccabcacbebebe"
k = 3
print("Longest substring length:", longest_substring_k_distinct(s, k))
