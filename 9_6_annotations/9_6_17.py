def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    result = {}
    for i in range(len(matrix)):
        result.setdefault(i + 1, matrix[i])
    return result

matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict(matrix))

matrix = [[5.1, 6, 7.94]]

print(matrix_to_dict(matrix))

annotations = matrix_to_dict.__annotations__

print(annotations['return'])