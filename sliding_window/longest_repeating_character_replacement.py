"""
Longest Repeating Character Replacement
LeetCode 424

Given a string s and an integer k, we can replace at most k characters.
Find the length of the longest substring that can contain the same
character after replacements.

Time Complexity: O(n)
Space Complexity: O(1) for uppercase English letters
"""


def character_replacement(s, k):
    i = 0
    j = 0
    freq = {}
    max_freq = 0
    maximum = 0

    while j < len(s):
        # Add current character to the window
        freq[s[j]] = freq.get(s[j], 0) + 1

        # Highest frequency seen in the current sliding process
        max_freq = max(max_freq, freq[s[j]])

        # Replacements needed = window size - most frequent character
        while (j - i + 1) - max_freq > k:
            freq[s[i]] -= 1

            if freq[s[i]] == 0:
                del freq[s[i]]

            i += 1

        maximum = max(maximum, j - i + 1)
        j += 1

    return maximum


s = "AABABBA"
k = 1

print(character_replacement(s, k))