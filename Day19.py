def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token in ['+', '-', '*', '/', '^']:
            right_operand = stack.pop()
            left_operand = stack.pop()
            
            if token == '+':
                result = left_operand + right_operand
            elif token == '-':
                result = left_operand - right_operand
            elif token == '*':
                result = left_operand * right_operand
            elif token == '/':
                if left_operand * right_operand < 0 and left_operand % right_operand != 0:
                    result = left_operand // right_operand + 1
                else:
                    result = left_operand // right_operand
            elif token == '^':
                result = left_operand ** right_operand
            
            stack.append(result)
        else:
            number = int(token)
            stack.append(number)
    
    return stack[0]

print(evaluate_postfix("15 7 1 1 + - / 3 * 2 1 1 + + -"))
