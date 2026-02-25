def count_anagram_occurrences(txt, pat):
    freq = {}
    for ch in pat:
        freq[ch] = freq.get(ch, 0) + 1

    count = len(freq)
    k = len(pat)
    i = 0
    ans = 0

    for j in range(len(txt)):

        if txt[j] in freq:
            freq[txt[j]] -= 1
            if freq[txt[j]] == 0:
                count -= 1

        if j - i + 1 == k:

            if count == 0:
                ans += 1

            if txt[i] in freq:
                if freq[txt[i]] == 0:
                    count += 1
                freq[txt[i]] += 1

            i += 1

    return ans


txt = "forxxrfoxrrfrofro"
pat = "for"
print("Anagram occurrences:", count_anagram_occurrences(txt, pat))
