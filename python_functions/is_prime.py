def is_prime(n):
  '''
  Return True if the input is prime, False otherwise
  Parameters
  ----------
  n: {int} input integer

  Returns
  -------
  is_prime: {bool} whether n is prime
  '''
  for num in range(1, n):
    if num != 1 and n % num == 0:
      return False
  return True