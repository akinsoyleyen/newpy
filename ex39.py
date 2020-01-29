states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Ditroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('_' * 10)
print('NY States has:', cities['NY'])
print('Oregon state has', cities['OR'])

#print out some states
print('_' * 10)
print('Michigans abbrevation is', states['Michigan'])
print('Floridas abbrevation is', states['Florida'])

#!Do it by using the state then cities dict
print('_' * 10)
print('Michigan has', cities[states['Michigan']]) #!Calling first from states dict and then from cities dict
print('Florida has', cities[states['Florida']])

#?print every state abbrevation
print('_' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')

#?print every city in state
for state, city in list(cities.items()):
    print(f'{city}s state is{state}')

#?Now do both at the same time
print('_' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbrevated {abbrev}')
    print(f'and has city {cities[abbrev]}')
print('_' * 10)

#safely get a abbrevation by state that might not be there
state = states.get('Texas')

if not state:
    print('Sorry, no Texas')

#get a state with a default value
city = cities.get('TX', 'Not Found')
print(f'The city for the state TX is: {city}')



