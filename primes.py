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

def nextelement(S):
  l = S[-1]
  for k in range(l + 1, 2*l):
    m = int(k**(1/2))
    for i in S:
      if (i > m):
        return k
      if (k%i == 0):
        break
        
def iterate(S):
  return S + [nextelement(S)]

def primesupto(N):
  S = [2]
  if (N <= 1):
    return []
  while (S[-1] <= N):
    S = iterate(S)
  return S[:-1]
