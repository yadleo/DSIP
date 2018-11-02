import numpy as np

def xtx_product(X):
  """
  Given a matrix X, calculate the inner product X^T X, where the ^T
  operator denotes the transpose.

  Parameters
  ----------
  X: NumPy array size of (n, m)

  Returns
  -------
  NumPy Array of size (m, m)
  """
  Xt = X[:]
  Xt = [[row[i] for row in Xt] for i in range(Xt.shape[1])]
  return np.dot(Xt, X)

print(xtx_product(np.array([[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]])))