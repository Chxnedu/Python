# a dictionary in python is a collection of key-value pairs
# to create a dictionary, call out the name and add some curly braces {} to it then list the key-value pairs

games = {
    'tlou' : 'A',
    'God of War' : 'A',
    'ghost of tsushima' : 'B'

}
# to call on a value in a dictionary, use dictionary_name['key']
rating = games['ghost of tsushima']
print('Ghost of Tsushima is a ' + games['ghost of tsushima'] + ' game')

# a better use case would be in a game
infectedHealth = {
    'Runner' : '20',
    'Stalker' : '15',
    'Clicker' : '35',
    'Shambler' : '50',
    'Bloater' : '75'
}

bloaterHealthBar = infectedHealth['Bloater']
print('the bloater has a huge health bar, its maximum health is ' + bloaterHealthBar)