import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Параметри симуляції
num_simulations = 1_000_000
min_sum = 2
max_sum = 12

# Імітація кидків двох кубиків
dice_rolls = np.random.randint(1, 7, size=(num_simulations, 2))
sums = np.sum(dice_rolls, axis=1)

# Підрахунок частоти появи кожної можливої суми
sum_counts = pd.Series(sums).value_counts().sort_index()
sum_probabilities = (sum_counts / num_simulations) * 100  # у відсотках

# Аналітичні дані для порівняння
analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}

# Створення таблиці з результатами
results_table = pd.DataFrame(
    {
        "Сума": range(min_sum, max_sum + 1),
        "Ймовірність (Монте-Карло)": [
            sum_probabilities.get(i, 0) for i in range(min_sum, max_sum + 1)
        ],
        "Ймовірність (Аналітична)": [
            analytical_probabilities[i] for i in range(min_sum, max_sum + 1)
        ],
    }
)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(
    results_table["Сума"],
    results_table["Ймовірність (Монте-Карло)"],
    marker="o",
    label="Монте-Карло",
)
plt.plot(
    results_table["Сума"],
    results_table["Ймовірність (Аналітична)"],
    marker="x",
    label="Аналітична",
)
plt.xlabel("Сума на кубиках")
plt.ylabel("Ймовірність (%)")
plt.title("Ймовірності сум при киданні двох кубиків")
plt.legend()
plt.grid(True)
plt.show()


print(results_table)
