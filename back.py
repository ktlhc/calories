proteins = float(input('Белки на 100 гр: '))
fats = float(input('Жиров на 100 гр: '))
carbohydrates = float(input('Углеводов на 100 гр: '))
calories = float(input('Килокалорий на 100 гр: '))
dry_mass = float(input('Масса сухого продукта (грамм): '))
ready_mass = float(input('Введите массу готового продукта (грамм): '))

# Расчет количества белков, жиров, углеводов и килокалорий на 100 грамм готового продукта
proteins_per_dry = proteins*dry_mass/100
fats_per_dry = fats*dry_mass/100
carbo_per_dry = carbohydrates*dry_mass/100
calories_per_dry = calories*dry_mass/100

proteins_per_ready = proteins_per_dry*100/ready_mass
carbo_per_ready = carbo_per_dry*100/ready_mass
fats_per_ready = fats_per_dry*100/ready_mass
calories_per_ready = calories_per_dry*100/ready_mass

# Вывод результатов
print('Белки на 100 грамм готового продукта:', proteins_per_ready)
print('Жиры на 100 грамм готового продукта:', fats_per_ready)
print('Углеводы на 100 грамм готового продукта:', carbo_per_ready)
print('Килокалории на 100 грамм готового продукта:', calories_per_ready)
