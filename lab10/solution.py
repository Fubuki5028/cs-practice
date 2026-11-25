import numpy as np

def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    mat = np.array(matrix)
    return mat[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    mat = np.array(matrix)
    mat[row_start:row_stop, column_start:column_stop] = value
    return mat.tolist()

def matrix_vector_product(matrix, vector):
    mat = np.array(matrix)
    vec = np.array(vector)
    return (mat @ vec).tolist()

def matrix_multiply(left, right):
    left_mat = np.array(left)
    right_mat = np.array(right)
    return (left_mat @ right_mat).tolist()

def transpose_matrix(matrix):
    return np.array(matrix).T.tolist()

def solve_system(matrix, vector):
    mat = np.array(matrix)
    vec = np.array(vector)
    return np.linalg.solve(mat, vec).tolist()

def tensor_channel_mean(tensor):
    t = np.array(tensor)
    result = np.mean(t, axis = -1)
    return result.tolist()

def point_distance(first, second):
    p1 = np.array(first)
    p2 = np.array(second)
    return  np.linalg.norm(p2 - p1).tolist()

if __name__ == "__main__":
    print(make_table(3,4))
