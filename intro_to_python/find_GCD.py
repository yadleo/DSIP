numOne, numTwo = int(input('Please enter a number: ')), int(input('Please enter another number: '))

result = 0;
smaller = 0;
if numOne >= numTwo:
  smaller = numTwo
else:
  smaller = numOne

while smaller > 0:
  if numOne % smaller == 0 and numTwo % smaller == 0:
    result = smaller
    break
  smaller -= 1

print(result)



#number = int(input('Please enter a number: '))
#number2 = int(input('Please enter another number: '))

#while number != number2:
#    if number > number2:
#        number -= number2
#    else:
#        number2 -= number

#print(number)
#The above is a basic implementation of Euclid's Algorithm

#A slightly more efficient implementation is as follows:

#number = int(input('Please enter a number: '))
#number2 = int(input('Please enter another number: '))

#while number2 != 0:
#    temp = number2
#    number2 = number % number2
#    number = temp    
#print(number)
#The second version runs much faster (~10x faster on my machine) because we skip many of the subtractions by using the modulus. An even more pythonic version of the above would use tuple unpacking to remove the temp variable:

#while number2 != 0:
#    number, number2 = number2, number % number2
#print(number)