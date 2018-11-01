# Input series of comma-separated strings
s = input('Please enter a series of comma-separated strings: ')
# Split on comma+space to create the list
l = s.split(', ')
l2 = list(l)
l2.reverse()
l.extend(l2)
# Convert list l into a palindrome and then print the list
print(l)