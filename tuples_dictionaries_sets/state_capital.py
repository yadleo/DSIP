state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau',
                    'California': 'Sacramento', 'Georgia': 'Atlanta',
                    'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                    'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}

capital = input('''Please enter a state: ''')

print(state_dictionary.get(capital.lower().title(), 'Capital unknown'))