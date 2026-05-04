import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)


def draw_koch_snowflake(order, size=300):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    screen.mainloop()


def main():
    level = int(input("Введіть рівень рекурсії (0-5): "))
    draw_koch_snowflake(level)


if __name__ == "__main__":
    main()