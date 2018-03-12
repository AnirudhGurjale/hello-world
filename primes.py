def isprime(p):
  if (p <= 1):
    return False
  if (p == 2)|(p == 3):
    return True
  k = int(p**(1/2))
  for i in range(2, k + 2):
    if (p%i == 0):
      return False
    if (i == k + 1):
      return True
