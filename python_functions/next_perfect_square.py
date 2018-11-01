def next_perfect_square(number):
  '''
  Returns the next perfect square of the input number, if the input number
  is not a perfect square, returns -1.
  Ex:
  next_perfect_square(10)
  >>> -1
  next_perfect_square(9)
  >>> 16
  next_perfect_square(25)
  >>> 36
  next_perfect_square(37)
  >>> -1

  Parameters
  ----------
  number: {int}

  Returns
  -------
  next_perfect: {int} the next perfect square, or -1 if number is not a
  perfect square
  '''
  if is_perfect_square(number) == False:
    return -1
  else:
    while is_perfect_square(number + 1) == False:
      number += 1
    return number + 1