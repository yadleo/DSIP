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

