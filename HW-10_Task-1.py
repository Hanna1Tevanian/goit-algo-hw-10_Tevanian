import pulp
 
limonad = pulp.LpVariable("Limonad", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')
 
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)
 
 # Функція максимізації (загальна кількість продуктів)
model += limonad + fruit_juice, "Total_Profit"
 
 # Додаємо обмеження на використання ресурсів
model += 2 * limonad + fruit_juice <= 100, "Water_Constraint"
model += limonad + fruit_juice <= 50, "Sugar_Constraint"
model += limonad <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"
 
model.solve()
 
print("Optimal Production Plan:")
print("Limonad:", pulp.value(limonad))
print("Fruit Juice:", pulp.value(fruit_juice))