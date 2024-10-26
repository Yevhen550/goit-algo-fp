items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    # Відсортуємо їжу за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    selected_items = []
    total_cost = 0
    total_calories = 0

    # Вибираємо їжу за жадібним принципом
    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return selected_items, total_calories


def dynamic_programming(items, budget):
    # Отримуємо всі назви їжі
    item_names = list(items.keys())
    n = len(item_names)

    # Створюємо таблицю для динамічного програмування
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо таблицю DP
    for i in range(1, n + 1):
        item = item_names[i - 1]
        cost = items[item]["cost"]
        calories = items[item]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                # Максимізуємо калорійність
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    # Відновлення обраних страв
    selected_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            item = item_names[i - 1]
            selected_items.append(item)
            b -= items[item]["cost"]

    total_calories = dp[n][budget]
    selected_items.reverse()  # Щоб зберегти порядок

    return selected_items, total_calories


# Тестування
budget = 100
print("Жадібний алгоритм:")
selected_greedy, calories_greedy = greedy_algorithm(items, budget)
print(f"Вибрані елементи: {selected_greedy}")
print(f"Загальна кількість калорій: {calories_greedy}")

print("\nДинамічне програмування:")
selected_dynamic, calories_dynamic = dynamic_programming(items, budget)
print(f"Вибрані елементи: {selected_dynamic}")
print(f"Загальна кількість калорій: {calories_dynamic}")
