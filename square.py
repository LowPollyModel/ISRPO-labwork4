def area(a):
    if a < 0:
        raise ValueError("Сторона квадрата не может быть отрицательной")
    return a * a

def perimeter(a):
    #Получаем на вход сторону квадрата. Возвращаем периметр фигуры
    return 4 * a

def main():
    print(area(int(input())))
    print(perimeter(int(input())))
    
if __name__ == "__main__":
    main()
