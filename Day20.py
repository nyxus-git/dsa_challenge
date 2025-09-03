def sortStack(stack):
   if len(stack) <= 1:
       return
   
   temp = stack.pop()
   sortStack(stack)
   insertInSortedOrder(stack, temp)

def insertInSortedOrder(stack, element):
   if len(stack) == 0 or element >= stack[-1]:
       stack.append(element)
       return
   
   temp = stack.pop()
   insertInSortedOrder(stack, element)
   stack.append(temp)

stack = [3, 1, 4, 2]
sortStack(stack)
print(stack)
