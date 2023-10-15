while True:
    is_composite = input('Блюдо составное? (да/нет): ')

    if is_composite.lower() == 'да':
        num_components = int(input('Сколько компонентов в блюде? '))
        total_proteins = 0
        total_fats = 0
        total_carbohydrates = 0
        total_calories = 0
        total_mass = 0
        ready_mass = float(input('Общая масса готового продукта (грамм): '))

        for i in range(num_components):
            print(f'Компонент {i+1}:')
            proteins_n = float(input('Белки на 100 гр: '))
            fats_n = float(input('Жиров на 100 гр: '))
            carbohydrates_n = float(input('Углеводов на 100 гр: '))
            calories_n = float(input('Килокалорий на 100 гр: '))
            mass = float(input('Масса компонента (гр): '))
            
            # расчет КБЖУ в каждом компоненте
            proteins = proteins_n * mass / 100
            fats = fats_n * mass / 100
            carbohydrates = carbohydrates_n * mass / 100
            calories = calories_n * mass / 100

            # расчет КБЖУ в массе компонентов
            total_proteins += proteins
            total_fats += fats
            total_carbohydrates += carbohydrates
            total_calories += calories
            total_mass += mass

        # расчет КБЖУ на 100 грамм для сухого продукта
       
        proteins_per_total = total_proteins * 100 / total_mass
        carbo_per_total = total_carbohydrates * 100 / total_mass
        fats_per_total = total_fats * 100 / total_mass
        calories_per_total = total_calories * 100 / total_mass
       
        # расчет КБЖУ на 100 грамм готового продукта

        proteins_per_ready = total_proteins * 100 / ready_mass
        carbo_per_ready = total_carbohydrates * 100 / ready_mass
        fats_per_ready = total_fats * 100 / ready_mass
        calories_per_ready = total_calories * 100 / ready_mass


        # вывод результатов расчета
        print('-----------------------------------------')   
        print('Белки на 100 грамм сырого продукта:', proteins_per_total)
        print('Жиры на 100 грамм сырого продукта:', fats_per_total)
        print('Углеводы на 100 грамм сырого продукта:', carbo_per_total)
        print('Килокалории на 100 грамм сырого продукта:', calories_per_total)

        print('Белки на 100 грамм готового продукта:', proteins_per_ready)
        print('Жиры на 100 грамм готового продукта:', fats_per_ready)
        print('Углеводы на 100 грамм готового продукта:', carbo_per_ready)
        print('Килокалории на 100 грамм готового продукта:', calories_per_ready)

    else:
        proteins_n = float(input('Белки на 100 гр: '))
        fats_n = float(input('Жиров на 100 гр: '))
        carbohydrates_n = float(input('Углеводов на 100 гр: '))
        calories_n = float(input('Килокалорий на 100 гр: '))
        total_mass = float(input('Общая масса сырого продукта (грамм): '))
        ready_mass = float(input('Масса готового продукта (грамм): '))

        # расчет КБЖУ в массе сырого продукта

        proteins_per_total = proteins_n * total_mass / 100
        carbohydrates_per_total = carbohydrates_n * total_mass / 100
        fats_per_total = fats_n * total_mass / 100
        calories_per_total = calories_n * total_mass / 100
       
        # расчет КБЖУ на 100 грамм готового продукта

        proteins_per_ready = proteins_per_total * 100 / ready_mass
        carbo_per_ready = carbohydrates_per_total * 100 / ready_mass
        fats_per_ready = fats_per_total * 100 / ready_mass
        calories_per_ready = calories_per_total * 100 / ready_mass
          
        # вывод результатов расчета
        print('-----------------------------------------')   
        print('Белки на 100 грамм готового продукта:', proteins_per_ready)
        print('Жиры на 100 грамм готового продукта:', fats_per_ready)
        print('Углеводы на 100 грамм готового продукта:', carbo_per_ready)
        print('Килокалории на 100 грамм готового продукта:', calories_per_ready)

    choice = input("Хотите ли вы повторить расчет? (да/нет): ")
    if choice.lower() != "да":
        break
