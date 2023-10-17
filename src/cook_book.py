def get_dict_in_file():
    cook_book = {}
    count = 0
    current_recipe = ''
    ingredient_keys = ['ingredient_name', 'quantity', 'measure']
    with open('files/recipes.txt') as f:
        for idx, line in enumerate(f):
            if idx == count:
                current_recipe = line.strip()
                cook_book[current_recipe] = []
                continue
            if idx == count + 1:
                # 2: строка заголовок, строка с количеством + кол-во строк с ингридиентами + 1: пустая строка
                count += 2 + int(line.strip()) + 1
                continue
            if not line.strip():
                continue
            ingredient_list = line.strip().split(' | ')
            ingredient_list[1] = int(ingredient_list[1])
            cook_book[current_recipe].append(dict(zip(ingredient_keys, ingredient_list)))
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_dict_in_file()
    ingredients_dict = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name in ingredients_dict:
                ingredients_dict[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
            else:
                ingredients_dict[ingredient_name] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}    
    return ingredients_dict