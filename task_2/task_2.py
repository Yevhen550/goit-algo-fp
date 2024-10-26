import turtle
import math


def draw_tree(branch_length, level, t):
    if level == 0:
        return

    # Намалювати стовбур
    t.forward(branch_length)

    # Повернути ліворуч і намалювати ліву гілку
    t.left(45)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1, t)

    # Повернути праворуч, щоб повернутися до стовбура,
    # а потім ще раз праворуч для правої гілки
    t.right(90)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1, t)

    # Повернутися до початкового положення
    t.left(45)
    t.backward(branch_length)


def main():
    # Налаштування вікна
    window = turtle.Screen()
    window.title("Фрактал 'Дерево Піфагора'")
    window.bgcolor("white")

    # Налаштування черепашки
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.left(90)  # Початковий напрямок - вверх
    t.up()
    t.goto(0, -200)  # Початкова позиція внизу екрана
    t.down()

    # Запитати рівень рекурсії у користувача
    level = int(input("Введіть рівень рекурсії (рекомендовано 5-10): "))

    # Почати малювання дерева
    draw_tree(100, level, t)

    # Залишити вікно відкритим після завершення малювання
    window.mainloop()


if __name__ == "__main__":
    main()
