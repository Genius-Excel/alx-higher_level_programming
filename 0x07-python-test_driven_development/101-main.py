#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

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
print(lazy_matrix_mul(matrix1, matrix2))


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


print(lazy_matrix_mul(matrix1, matrix2))

print(lazy_matrix_mul([[]], []))

print(lazy_matrix_mul([[1, 2, 3]], [[]]))

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

print(lazy_matrix_mul(matrix1, matrix2))

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

print(lazy_matrix_mul(matrix1, matrix2))


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

print(lazy_matrix_mul(matrix1, matrix2))

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

print(lazy_matrix_mul(matrix1, matrix2))
