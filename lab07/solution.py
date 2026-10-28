import numpy as np

def reshape_rows(values, width):
    if not values or width <= 0 or len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype = float)
    reshape = arr.reshape(-1, width)
    return reshape.tolist()

def block(matrix, rows, columns):
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype = float)
    matrix2 = arr[np.ix_(rows, columns)]
    return matrix2.tolist()

def column_means(matrix):
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype = float)
    result = np.mean(arr, axis = 0)
    return np.round(result, 6).tolist()


def column_range(matrix, column):
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype = float)
    col = arr[:, column]
    result = np.max(col) - np.min(col)
    return float(np.round(result, 6))



if __name__ == "__main__":
    print(reshape_rows([12, 14.5, 11, 13, 15.5, 10.5], 3))
    print(reshape_rows([1, 2, 3], 2))
    print(reshape_rows([], 3))
    print(reshape_rows([1, 2, 3, 4], 2))
    print(block([[1, 2], [3, 4]], [1, 0], [1, 0]))
    print(column_means([[1, 2], [3, 4], [5, 6]]))
    print(column_means([[1.5, 2.5]]))
    print(column_means([]))
    print(column_range([[1, 2], [5, 7]], 1))
    print(column_range([[3, 3], [3, 3]], 0))
