def getPermutations(string):
    chars = sorted(string) 
    result = []
    used = [False] * len(chars)
    backtrack(chars, [], used, result)
    return result

def backtrack(chars, currentPermutation, used, result):
    if len(currentPermutation) == len(chars):    
        result.append(''.join(currentPermutation)) 
        return
    
    for i in range(len(chars)):  
        if used[i]:
            continue
        if i > 0 and chars[i] == chars[i-1] and not used[i-1]:
            continue
        
        currentPermutation.append(chars[i])  
        used[i] = True 
        backtrack(chars, currentPermutation, used, result)
        currentPermutation.pop()
        used[i] = False 

print(getPermutations("abc"))
