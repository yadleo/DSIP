# Input series of comma-separated strings
s = input('Please enter a series of comma-separated strings: ')
# Split on comma+space to create the list
l = s.split(', ')
# Convert list l into an odd-length palindrome and then print the list
l2 = list(l)
l2.pop()
l2.reverse()
l.extend(l2)
print(l)