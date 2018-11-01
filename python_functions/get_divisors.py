def get_divisors(n):
  '''
  This function calculates and returns all of the divisors of n, between 1 and
  n, inclusive.

  Parameters
  ----------
  n: {int}

  Returns
  -------
  divisors: {list} all divisors of n in order from smallest to largest
  '''
  divisors = []
  for int in range(1, n + 1):
    if n % int == 0:
      divisors.append(int)
  return divisors