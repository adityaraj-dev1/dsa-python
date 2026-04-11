def longest_unique_substring(s):
    i = 0
    char_set = set()
    max_len = 0

    for j in range(len(s)):
        while s[j] in char_set:
            char_set.remove(s[i])
            i += 1

        char_set.add(s[j])
        max_len = max(max_len, j - i + 1)

    return max_len


s = "abcabcbb"
print("Longest unique substring length:", longest_unique_substring(s))
