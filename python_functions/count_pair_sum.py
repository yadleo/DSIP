def count_pair_sums(arr, number=0):
  '''
  Given an array, find the count of how many pairs of numbers in the array sum
  to the input number

  Parameters
  ----------
  arr: {list} list of integers (positive and negative)
  number: number to see if pairs sum to (default 0)

  Returns
  -------
  {int} the number of pairs found that sum to given number
  '''
  count = 0
  for idx, int1 in enumerate(arr):
    temp = arr[idx + 1:]
    for int2 in temp:
      if check_sum(int1, int2, number):
        count += 1
  return count

def check_sum(num1, num2, sum):
  return num1 + num2 == sum

# count_pair_sums([1,2,3,4,5], 5)
# check_sum(1, -1, 0)