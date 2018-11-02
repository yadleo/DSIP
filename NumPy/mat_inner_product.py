import numpy as np

def mat_inner_product(X, Y):
  '''
  Multiply two numpy arrays, if possible.

  Parameters
  ----------
  X: array, shape (n, m)
  Y: array, shape (p, q)

  Returns
  -------
  ret: array, shape (n, q), or False
      If the two arrays cannot be multiplied (X times Y), then return False.
      Otherwise return the product.
  '''
  if X.shape[1] != Y.shape[0]:
    return False
  else:
    return np.dot(X, Y)

mat1 = np.array([[3,2],[7,4],[9,1]])
mat2 = np.array([[2, -1, 3, 0], [-2, 0, -1, 4]])

print(mat_inner_product(mat1, mat2))
