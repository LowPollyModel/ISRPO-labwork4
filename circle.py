import math


def area(r):
    if r < 0:
        raise ValueError("Радиус круга не может быть отрицательным")
    #Получаем на вход радиус круга. Возвращаем площадь всей фигуры
    return math.pi * r * r


def perimeter(r):
    #Получаем на вход радиус круга. Возвращаем длину окружности
    return 2 * math.pi * r

def main():
    print(area(int(input())))
    print(perimeter(int(input())))
    
if __name__ == "__main__":
    main()
