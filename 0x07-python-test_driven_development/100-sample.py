#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

print("my test cases......")

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 4, 5],
    [3, 2, 1]
]
print(matrix_mul(matrix1, matrix2))


matrix1 = [
    [1.5, 2.8, 3.3],
    [4.0, 5, 6.7],
    [7.8, 8.9, 9.5]
]
matrix2 = [
    [9.09, 8.7, 7],
    [6.5, 9, 4],
    [3.8, 2, 0]
]


print(matrix_mul(matrix1, matrix2))

print(matrix_mul([[]], []))

print(matrix_mul([[1, 2, 3]], [[]]))

matrix1 = [
    (1, 2, 3),
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(matrix_mul(matrix1, matrix2))

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = (
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
)

print(matrix_mul(matrix1, matrix2))


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5],
    [3, 2, 1]
]

print(matrix_mul(matrix1, matrix2))

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, '5', 4],
    [3, 2, 1]
]

print(matrix_mul(matrix1, matrix2))
