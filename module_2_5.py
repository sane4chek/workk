def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        array = []
        for j in range(m):
            array.append(value)
        matrix.append(array)
    return matrix


matrix = get_matrix(3, 5, "werty")
print(matrix)

