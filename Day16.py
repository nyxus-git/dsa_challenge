def eclideanFunction(a, b):
  while b != 0:
    temp = b
    b= a % b
    a = temp
  return a
def findLCMofTwoNumbers(a,b):
  gcd_value = eclideanFunction(a,b)
  lcm_value = int((a * b) / gcd_value)
  return lcm_value
  
print(eclideanFunction(4, 6))
