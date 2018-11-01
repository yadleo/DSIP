number = int(input('Please enter a number: '))

result = 1
while number > 1:
  result *= number
  number -= 1
print(result)


#number = int(input('Please enter a number: '))

#result = 1
#count = 1
#while count <= number:
#    result *= count
#    count += 1
#print(result)
#An alternate method:

#number = int(input('Please enter a number: '))

#result = 1
#while number > 0:
#    result *= number
#    number -= 1
#print(result)
#Both of these pass the tests and compute factorials. Neither give the incorrect result for 0!. They both give 1 as the result for any negative input. This is perhaps undesirable; later in the course you learn how to write code that rejects improperly formatted values. After that, you can write code so that it throws an error when a negative value is inputted to compute the factorial of.