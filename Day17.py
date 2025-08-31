def primeFactorization(n):
  factor = []
  current_number = n

  while current_number % 2 == 0:
    factor.append(2)
    current_number = current_number // 2

  divisor = 3
  while divisor * divisor <= current_number:
    while current_number % divisor == 0:
      factor.append(divisor)
      current_number = current_number // divisor

    divisor += 2

  if current_number > 1:
        factor.append(current_number)
    
  return factor

for num in [30, 49, 19, 64, 123456,27]:
  print(primeFactorization(num))
