# parameter-defaults-starter
# Henry Roeser
# 11/18/24

# 8-3 T-Shirt
def make_shirt(shirt_size, shirt_text):
    print(f'The shirt is a size {shirt_size} and the text on the shirt is {shirt_text}.')
make_shirt('small','brocode')
make_shirt(shirt_text = 'brocode', shirt_size = 'small')

# 8-4 Large Shirts
def make_shirt(shirt_text, shirt_size = 'Large'):
    print(f'The shirt is a size {shirt_size} and the text on the shirt is {shirt_text}.')
make_shirt('I love Python')
make_shirt('I love Python','medium')

# 8-5 Cities
def describe_city(city, country = 'Russia'):
    print(f'{city} is in {country}.')
describe_city('Moscow')
describe_city('Kazan')
describe_city('Traverse')
