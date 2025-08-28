def longestSubstring(s, k):
    n = len(s)
    ans = 0

    for i in range(n):
        freq = {}
        distinct = 0
        countAtLeastK = 0

        for j in range(i, n):
            ch = s[j]

            if ch not in freq:
                freq[ch] = 0
                distinct += 1

            freq[ch] += 1

            if freq[ch] == k:
                countAtLeastK += 1

            if countAtLeastK == distinct:
                length = j - i + 1
                if length > ans:
                    ans = length

    return ans
