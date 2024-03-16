from pulp import *

# Створення проблеми LP максимізації
problem = LpProblem("Максимізація виробництва", LpMaximize)

# Визначення змінних для кількості "Лимонаду" та "Фруктового соку"
limonad = LpVariable("Лимонад", lowBound=0, cat='Integer')
frukt_sok = LpVariable("Фруктовий сік", lowBound=0, cat='Integer')

# Визначення змінних для кількості використаних ресурсів для "Лимонаду"
water_for_limonad = LpVariable("Вода для Лимонаду", lowBound=0, cat='Integer')
sugar_for_limonad = LpVariable("Цукор для Лимонаду", lowBound=0, cat='Integer')
lemon_juice_for_limonad = LpVariable("Лимонний сік для Лимонаду", lowBound=0, cat='Integer')

# Визначення змінних для кількості використаних ресурсів для "Фруктового соку"
fruit_puree_for_sok = LpVariable("Фруктове пюре для Фруктового соку", lowBound=0, cat='Integer')
water_for_sok = LpVariable("Вода для Фруктового соку", lowBound=0, cat='Integer')

# Додавання функції максимізації (загальна кількість продуктів)
problem += limonad + frukt_sok, "Загальна кількість продуктів"

# Додавання умови для виробництва "Лимонаду"
problem += 2*water_for_limonad + sugar_for_limonad + lemon_juice_for_limonad == limonad, "Виробництво Лимонаду"

# Додавання умови для виробництва "Фруктового соку"
problem += 2*fruit_puree_for_sok + water_for_sok == frukt_sok, "Виробництво Фруктового соку"

# Додавання обмежень на ресурси
problem += water_for_limonad + water_for_sok <= 100, "Обмеження на воду"
problem += sugar_for_limonad <= 50, "Обмеження на цукор"
problem += lemon_juice_for_limonad <= 30, "Обмеження на лимонний сік"
problem += fruit_puree_for_sok <= 40, "Обмеження на фруктове пюре"

# Розв'язання проблеми
problem.solve()

# Виведення результатів
print("Кількість 'Лимонаду':", value(limonad))
print("Кількість 'Фруктового соку':", value(frukt_sok))
