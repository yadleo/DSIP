words = input('''Please enter words seperated by commas: ''')

words = set(words.split(', '))

print(', '.join(words))