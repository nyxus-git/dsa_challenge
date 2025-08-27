def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
    return res

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("a"))
print(longestPalindrome("aaaa"))
print(longestPalindrome("abc"))
