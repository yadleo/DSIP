nums = input('''Please enter a series of numbers separated by commas. \n Hit enter when you are done. ''')

nums = nums.split(', ')
for idx, num in enumerate(nums):
  nums[idx] = int(num)
if len(nums) % 2 != 0:
  nums.pop()

even = nums[::2]
odd = nums[1::2]

list_tuple = list(zip(even, odd))
print(list_tuple)