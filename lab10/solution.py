import numpy as np

def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    mat = np.array(matrix)
    return mat[row_start:row_stop, column_start:column_stop].tolist()



if __name__ == "__main__":
    print(make_table(3,4))
