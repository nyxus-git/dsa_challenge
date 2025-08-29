def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        current_char = s[right]

        if current_char in char_map and char_map[current_char] >= left:
            left = char_map[current_char] + 1
        

        char_map[current_char] = right
        current_length = right - left + 1
        max_length = max(max_length, current_length)
    return max_length

print(f'Input: "abcabcbb", Output: {lengthOfLongestSubstring("abcabcbb")}')
print(f'Input: "bbbbb", Output: {lengthOfLongestSubstring("bbbbb")}')      
print(f'Input: "pwwkew", Output: {lengthOfLongestSubstring("pwwkew")}')    
print(f'Input: "abcdefgh", Output: {lengthOfLongestSubstring("abcdefgh")}')
print(f'Input: "a", Output: {lengthOfLongestSubstring("a")}')              
