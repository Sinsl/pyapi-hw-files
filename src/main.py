from pprint import pprint
from cook_book import *
from sort import *

print('\nЗадача 1\n')
cook_book = get_dict_in_file()    
pprint(cook_book)

print('\nЗадача 2\n')
ingredients_dict = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
pprint(ingredients_dict)

print('\nЗадача 3\n')
sort_text_files()
with open('files/story.txt') as f:
    data = f.read()
    print(data)