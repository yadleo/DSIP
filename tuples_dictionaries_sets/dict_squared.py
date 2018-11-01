nums = input('''Please enter a series of numbers separated by '-'. \n Hit enter when you are done. ''')

nums = nums.split('-')
for idx, num in enumerate(nums):
  nums[idx] = int(num)
squared_dict = {num: num * num for num in nums}
print(squared_dict)