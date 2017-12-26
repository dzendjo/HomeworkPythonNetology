cook_book = dict()
with open('data.txt', encoding='utf-8') as f:
    raw_data = f.read()
blocks = []
i = 0
for block in raw_data.split('\n\n'):
    blocks.append(block)

for block in blocks:
    one_receipt = block.split('\n')
    # print(one_receipt)
    list_of_ingredients = []

    for i in range(2, len(one_receipt)):
       current_ingredient = one_receipt[i].split(' | ')
       list_of_ingredients.append({'ingredient_name': current_ingredient[0],
                                   'quantity': current_ingredient[1],
                                   'measure': current_ingredient[2]})
    cook_book[one_receipt[0]] = list_of_ingredients

print('Название блюда: Омлет\nРецепт: {}'.format(cook_book['Омлет']))
print('Название блюда: Фахитос\nРецепт: {}'.format(cook_book['Фахитос']))



# cook_book = {
#   'яйчница': [
#     {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#     {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#     ],
#   'стейк': [
#     {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#     {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#     {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#     ],
#   'салат': [
#     {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#     {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#     {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#     {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#     ]
#   }