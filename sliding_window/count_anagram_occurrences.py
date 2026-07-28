"""
Problem: Count Occurrences of Anagrams

Given a text and a pattern, count the number of substrings in the text
that are anagrams of the pattern.

Approach 1: Brute Force
Time Complexity: O(n * k)
Space Complexity: O(k)

Approach 2: Sliding Window + Frequency Map
Time Complexity: O(n)
Space Complexity: O(k)
"""


# -------------------- Brute Force --------------------

def count_anagrams_brute(text, pattern):
    # Frequency map of pattern
    freq1 = {}
    for ch in pattern:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1

    count = 0
    k = len(pattern)

    # Check every window
    for i in range(len(text) - k + 1):
        freq2 = {}

        for j in range(i, i + k):
            ch = text[j]
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1

        if freq1 == freq2:
            count += 1

    return count


# -------------------- Optimal --------------------

def count_anagrams_optimal(text, pattern):
    freq = {}

    # Frequency map of pattern
    for ch in pattern:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    count = len(freq)
    result = 0

    k = len(pattern)

    i = 0
    j = 0

    while j < len(text):

        # Process incoming character
        if text[j] in freq:
            freq[text[j]] -= 1
            if freq[text[j]] == 0:
                count -= 1

        # Expand window
        if j - i + 1 < k:
            j += 1

        # Window size becomes k
        elif j - i + 1 == k:

            if count == 0:
                result += 1

            # Remove outgoing character
            if text[i] in freq:
                if freq[text[i]] == 0:
                    count += 1
                freq[text[i]] += 1

            i += 1
            j += 1

    return result


# -------------------- Driver Code --------------------

text = "forxxorfxrfox"
pattern = "for"

print("Brute Force :", count_anagrams_brute(text, pattern))
print("Optimal     :", count_anagrams_optimal(text, pattern))