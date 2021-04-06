# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __add__(self):
        new_matr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(self.list1)):
            for j in range(len(self.list1[i])):
                new_matr[i][j] = self.list1[i][j] + self.list2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i])for i in new_matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i])for i in new_matr]))


my_matrix = Matrix([[19, 18, 17], [16, 15, 14], [13, 12, 11]], [[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print(my_matrix.__add__())
