def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)

get_matrix(5, 7, 63)
get_matrix(6, 4, 15)
get_matrix(2, 3, 18)
get_matrix(3, 2, 11)
