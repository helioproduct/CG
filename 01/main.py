import numpy as np
import matplotlib.pyplot as plt

# Ввод констант a, b, k, A, B
a = float(input("Введите значение a > 0: "))
B = float(input("Введите значение B: "))

# Генерируем значения x в заданном диапазоне [0, B]
x = np.linspace(0, B, 1000)

# Рассчитываем соответствующие значения y
y = a * np.power(x, 1.5)

# Строим график
plt.plot(x, y, label=f"y = {a}x^(3/2)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Кривая y=ax^(3/2)")
plt.grid(True)
plt.legend()
plt.show()
