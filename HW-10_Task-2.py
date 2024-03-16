import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Генерація випадкових точок
n = 10000  # Кількість точок
x_values = np.random.uniform(a, b, n)
y_values = np.random.uniform(0, f(b), n)  # Генеруємо y у межах [0, f(b))

# Обчислення кількості точок, які потрапляють під криву
count_under_curve = np.sum(y_values <= f(x_values))

# Обчислення площі сірої зони (під кривою)
area_rectangle = (b - a) * f(b)  # Площа прямокутника
area_gray_zone = (count_under_curve / n) * area_rectangle

print("Площа сірої зони (Метод Монте-Карло):", area_gray_zone)

# Обчислення інтеграла методом quad
result_quad, _ = spi.quad(f, a, b)

print("Інтеграл (quad):", result_quad)

# Порівняння результатів
print("Різниця між методом Монте-Карло та quad:", abs(area_gray_zone - result_quad))
