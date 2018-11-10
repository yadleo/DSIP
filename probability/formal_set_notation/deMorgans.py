def deMorgans(E, F, S):
  '''
  Return, as a tuple of the form (Law A, Law B), each of the sets
  associated with De Morgan's laws as applied to sets E and F.

  Return "Improper Specification" if three sets are not supplied
  or if the events E and F are not subsets of the sample space S.
  
  Parameters
  ----------
  E : {set} First event space
  F : {set} Second event space
  S : {set} Complete sample space

  Returns
  -------
  tuple({set}, {set}) or {str} 

  Example:
  >>> DeMorgans(set([1,2,3]), set([2,3,4]), set([0,1,2,3,4,5]))
  (set([0, 5]), set([0, 1, 2, 4, 5])
  '''

  if check_specs(E, F, S) == "fail":
    return "Improper Specification"
  else:
    law_a = lawA(E, F, S)
    law_b = lawB(E, F, S)
  return (law_a, law_b)


def check_specs(E, F, S):
  # check if set E and set F is a subset of S
  if not E.issubset(S) or not F.issubset(S):
    return "fail"
  if not isinstance(E, set) or not isinstance(F, set) or not isinstance(S, set):
    return "fail"
  return 'pass'
# returns the complement of the union of set E and set F
def lawA(E, F, S):
  return S.difference(E.union(F))

# returns the complement of the intersection of set E and set F
def lawB(E, F, S):
  return S.difference(E.intersection(F))