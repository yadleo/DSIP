# Input series of comma-separated strings
s = input('Please enter a series of comma-separated strings: ')
# Split on comma+space to create the list
l = s.split(', ')

# Sort l, then print the elements of l in numbered fashion, starting at 1
l.sort()
for idx, elem in enumerate(l):
  print(idx + 1, elem)