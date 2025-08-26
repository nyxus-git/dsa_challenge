def validParanthesis(s):
    bracket_map = {')': '(', '}': '{', ']': '['}  
    stack = []

    if len(s) % 2 != 0:
        return False

    for char in s:
        if char in bracket_map:
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
        else: 
            stack.append(char)

    return not stack
  
print(validParanthesis("()"))      
print(validParanthesis("([)]"))    
print(validParanthesis("[{()}]"))  
print(validParanthesis("{[}"))     
print(validParanthesis(""))        
print(validParanthesis("("))       
print(validParanthesis("((("))     
print(validParanthesis(")"))       
