import numpy as np

# Задание 1. Создание векторов и матриц
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print(hours)
print(hours.shape, hours.ndim, hours.size, hours.dtype)
print(line)
print(zeros)
print(unknown_table)
print(identity)

# Задание 2. Индексы и срезы в векторе
print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])

# Задание 3. Строки и столбцы таблицы
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)

print(temperatures[2])
print(temperatures[:, 2])
print(temperatures[0])
print( temperatures[:, -1])
print(temperatures[:2, :2])

central_fragment = temperatures[0:2, 1:3]
print(central_fragment)
print(central_fragment.shape)
print(central_fragment.tolist())

# Задание 4. Прямоугольные срезы
matrix = np.arange(1, 26).reshape(5, 5)
print(matrix)

slice1 = matrix[:3, :]
print(slice1.shape,slice1)

slice2 = matrix[-2:, :]
print(slice2.shape, slice2)

slice3 = matrix[:, :2]
print(slice3.shape, slice3)

slice4 = matrix[1:4, 2:5]
print(slice4.shape, slice4)

slice5 = matrix[-2:, -2:]
print(slice5.shape, slice5)

# Задание 5. Изменение массива с помощью срезов
print("--- Задание 5 ---")
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print(changed_hours)
print(hours)

changed_matrix = matrix.copy()
changed_matrix[-1, :] = -1
changed_matrix[1:4, 1:4] = 100

print(changed_matrix)
print(matrix)

# hours не изменился, так как мы сделали независимую копию через .copy()

# Задание 6. Изменение формы
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print(numbers)
print(table)
print(transposed)

# table.reshape(3, 4) работает, потому что общее количество элементов в numbers (12)
# table.reshape(5, 3) выдаст ошибку, потому что 5 * 3 = 15, а элементов в массиве только 12.