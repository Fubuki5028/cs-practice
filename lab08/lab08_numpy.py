import numpy as np

# ==========================================
# Задание 1. Создание векторов и матриц
# ==========================================
print("--- Задание 1 ---")
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("Свойства hours: shape =", hours.shape, ", ndim =", hours.ndim, ", size =", hours.size, ", dtype =", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)
print()

# ==========================================
# Задание 2. Индексы и срезы в векторе
# ==========================================
print("--- Задание 2 ---")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])
print()