def count_divisors(n):
  if n == 1:
    return 1

  count = 0
  i = 1

  while i * i <= n:
    if n % i == 0:
      if i * i == n:
        count += 1
      else:
        count += 2

    i += 1

  return count

print(count_divisors(18))
print(count_divisors(29))
print(count_divisors(100))
print(count_divisors(1))
print(count_divisors(10000000000000))
