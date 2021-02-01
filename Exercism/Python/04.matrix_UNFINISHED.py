"""https://exercism.io/tracks/python/exercises/matrix
Given a string representing a matrix of numbers, return the rows and columns of that matrix. 
So given a string with embedded newlines like:
9 8 7
5 3 2
6 6 7
representing this matrix:
    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2
3 | 6  6  7
your code should be able to spit out:
- A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
- A list of the columns, reading each column top-to-bottom while moving from left-to-right.
The rows for our example matrix:
9, 8, 7
5, 3, 2
6, 6, 7
And its columns:
9, 5, 6
8, 3, 6
7, 2, 7
"""


class Matrix():
    "Common class for matrix"

    def __init__(self, mtx_str):
        self.mtx_str = mtx_str
        self.mtx_rows = self.mtx_rows()
        self.mtx_cols = ""
        self.mtx_dim = (0, 0)
    
    def mtx_rows(self):
        return self.mtx_str.replace(' ', ', ')

    def mtx_cols(self):
        self.mtx_cols = ""

    def calculate_dim(self):
        self.mtx_dim = (len(self.mtx_str.splitlines()[0].split()), len(self.mtx_str.splitlines()))
    
    def print_mtx_infos(self):
        print(f'String representation:\n{self.mtx_str}\nDimensions: {self.mtx_dim}\n', \
            f'The rows of the matrix:\n{self.mtx_rows}\nThe cols of the matrix:\n{self.mtx_cols}', sep = '')


def main():
    our_matrix = Matrix("9 8 7\n5 3 2\n6 6 7\n8 6 7")
    our_matrix.calculate_dim()
    our_matrix.print_mtx_infos()


if __name__ == "__main__":
    main()

"""
class Matrix(object):

    def __init__(self, matrix_string):
        self.rows = [[int(j) for j in row.split()] for row in matrix_string.split('\n')]

    def row(self, row_number):
        return self.rows[row_number - 1]
    
    def column(self, column_number):
        return [row[column_number-1] for row in self.rows]


our_matrix = Matrix("9 8 7\n5 3 2\n6 6 7\n8 6 7")
print(our_matrix.row)()
"""
