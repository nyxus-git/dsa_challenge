def group_anagrams(strs):
    anagram_groups = {}
    
    for word in strs:
        sorted_chars = ''.join(sorted(word))
        
        if sorted_chars not in anagram_groups:
            anagram_groups[sorted_chars] = []
        
        anagram_groups[sorted_chars].append(word)
    
    return list(anagram_groups.values())

test_input =  ["abc", "def", "ghi"]
print(group_anagrams(test_input))
