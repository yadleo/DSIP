numOne, numTwo = int(input('Please enter a number: ')), int(input('Please enter another number: '))

result = 1
smaller = 0
larger = 0
if numOne >= numTwo:
  smaller = numTwo
  larger = numOne
else:
  smaller = numOne
  larger = numTwo

counter = smaller

#if smaller is a divisor of larger
#larger is the LCM

#if counter is less than or equal to smaller
#if counter is a divisor for both smaller and larger
#multiple the result with counter
#set smaller and larger as quotient of counter

while counter > 0:
  if smaller % counter == 0 and larger % counter == 0:
    result *= counter
    smaller = smaller / counter
    larger = larger / counter
  counter -= 1
result = result * smaller * larger

print(result)




#number = int(input('Please enter a number: '))
#number2 = int(input('Please enter another number: '))

#a, b = number, number2
#while number != number2:
#    if number > number2:
#        number -= number2
#    else:
#        number2 -= number

#result = (a / number) * b

#print(result)

#Here you reused your answer to the previous problem. This is a common practice, and in future lessons you learn about the value of abstracting away some of this reuse as functions.

#Once you have the GCD, you can compute the LCM as (n1 * n2 / gcd(n1, n2)). Because your algorithm for computing GCD modifies the numbers, you save copies of them as a and b before you compute it so you can reliably calculate the LCM.