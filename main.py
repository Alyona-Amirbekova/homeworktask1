cook_book={}
with open('recipes.txt', 'r', encoding='utf-8') as f:
    while True:
        # Читаем название блюда
        dish = f.readline().strip()
        if not dish:
            break

        # Читаем количество ингредиентов
        count = int(f.readline().strip())

        # Читаем ингредиенты
        ingredients = []
        for _ in range(count):
            parts = f.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': parts[0],
                'quantity': int(parts[1]),
                'measure': parts[2]
            })

        # Добавляем в словарь
        cook_book[dish] = ingredients

        # Пропускаем пустую строку между рецептами
        f.readline()
    print(cook_book)

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}

        for dish_name in dishes:
            if dish_name not in cook_book:
                print(f"Блюдо '{dish_name}' не найдено!")
                continue

            for ingredient in cook_book[dish_name]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}

        return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
