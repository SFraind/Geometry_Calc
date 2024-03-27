import geometry_calculator

def main():
    while True:
        print("Выберите тип фигуры:")
        print("1. Круг")
        print("2. Прямоугольник")
        print("3. Треугольник")
        print("4. Выйти")

        choice = input("Введите номер выбранной фигуры: ")

        if choice == "1":
            radius = float(input("Введите радиус круга: "))
            area = geometry_calculator.calculate_area(radius)
            print(f"Площадь круга с радиусом {radius} равна {area:.2f}")
        elif choice == "2":
            length = float(input("Введите длину прямоугольника: "))
            width = float(input("Введите ширину прямоугольника: "))
            area = geometry_calculator.calculate_area(length, width)
            print(f"Площадь прямоугольника с длиной {length} и шириной {width} равна {area:.2f}")
        elif choice == "3":
            side1 = float(input("Введите длину первой стороны треугольника: "))
            side2 = float(input("Введите длину второй стороны треугольника: "))
            side3 = float(input("Введите длину третьей стороны треугольника: "))
            area = geometry_calculator.calculate_area(side1, side2, side3)
            print(f"Площадь треугольника со сторонами {side1}, {side2} и {side3} равна {area:.2f}")
        elif choice == "4":
            print("Завершение работы.")
            break
        else:
            print("Некорректный выбор фигуры.")

        next_action = input("Желаете продолжить? Нажмите 1 для продолжения: ")
        if next_action != "1":
            print("Завершение работы.")
            break


if __name__ == "__main__":
    main()
