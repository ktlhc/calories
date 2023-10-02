is_composite = input('Блюдо составное? (да/нет): ')

if is_composite.lower() == 'да':
    num_components = int(input('Сколько компонентов в блюде? '))
    total_proteins = 0
    total_fats = 0
    total_carbohydrates = 0
    total_calories = 0
    total_mass = 0
    ready_mass = float(input('Общая масса продукта (грамм'))
    for i in range(num_components):
        print(f'Компонент {i+1}:')
        proteins = float(input('Белки на 100 гр: '))
        fats = float(input('Жиров на 100 гр: '))
        carbohydrates = float(input('Углеводов на 100 гр: '))
        calories = float(input('Килокалорий на 100 гр: '))
        mass = float(input('Масса компонента (грамм): '))
        total_mass += mass
        total_proteins += proteins
        total_fats += fats
        total_carbohydrates += carbohydrates
        total_calories += calories
    
    proteins_per_ready = total_proteins*100/ready_mass
    carbo_per_ready = total_carbohydrates*100/ready_mass
    fats_per_ready = total_fats*100/ready_mass
    calories_per_ready = total_calories*100/ready_mass
    
    print('Белки на 100 грамм готового продукта:', proteins_per_ready)
    print('Жиры на 100 грамм готового продукта:', fats_per_ready)
    print('Углеводы на 100 грамм готового продукта:', carbo_per_ready)
    print('Килокалории на 100 грамм готового продукта:', calories_per_ready)
    
else:
     proteins = float(input('Белки на 100 гр: '))
     fats = float(input('Жиров на 100 гр: '))
     carbohydrates = float(input('Углеводов на 100 гр: '))
     calories = float(input('Килокалорий на 100 гр: '))
     ready_mass = float(input('Общая масса продукта (грамм):'))

     proteins_per_ready = proteins*100/ready_mass
     carbo_per_ready = carbohydrates*100/ready_mass
     fats_per_ready = fats*100/ready_mass
     calories_per_ready = calories*100/ready_mass
    
     print('Белки на 100 грамм готового продукта:', proteins_per_ready)
     print('Жиры на 100 грамм готового продукта:', fats_per_ready)
     print('Углеводы на 100 грамм готового продукта:', carbo_per_ready)
     print('Килокалории на 100 грамм готового продукта:', calories_per_ready)
