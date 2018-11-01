nums1 = input('''Please enter numbers separated by commas: ''' )
nums2 = input('''Please enter another set of numbers separated by commas: ''' )

nums1 = nums1.split(', ')
nums2 = nums2.split(', ')

for idx, num in enumerate(nums1):
  nums1[idx] = int(num)

for idx, num in enumerate(nums2):
  nums2[idx] = int(num)

num1 = set(nums1)
num2 = set(nums2)

intersect = num1.intersection(num2)
result = []
for num in intersect:
  result.append(num)
result.sort()
for idx, num in enumerate(result):
  result[idx] = str(num)

print(', '.join(result))