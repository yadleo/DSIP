# Input series of comma-separated strings
s1 = input('Please enter a series of comma-separated strings: ')
# Split on comma+space to create the list
l = s1.split(', ')
# Input the string to count in the list
s2 = input('Please enter a string to count: ')

# Print out the number of times s2 occurs in s1
print(s1.count(s2))