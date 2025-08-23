def prefixFindout(words):
    word = ""
    if len(words) == 0:
        return ""
    
    min_length = min(len(w) for w in words)
    
    for position in range(min_length):
        first_char = words[0][position]
        for j in range(1, len(words)):
            if words[j][position] != first_char:
                return word
        word = word + first_char
    return word

arr =  ["alone"]
print(prefixFindout(arr))
