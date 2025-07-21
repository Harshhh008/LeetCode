# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         row_zero = set()
#         col_zero = set()

#         for row in range(len(matrix)):
#             for col in range(len(matrix[row])):
#                 if matrix[row][col] == 0:
#                     row_zero.add(row)
#                     col_zero.add(col)

#         print(row_zero, col_zero)

#         for row in row_zero:
#             for col in range(len(matrix[0])):
#                 matrix[row][col] = 0

#         for col in col_zero:
#             for row in range(len(matrix)):
#                 matrix[row][col] = 0




class Solution:
#[1,  2,  3,  4],
#[5,  0,  7,  8],
#[0, 10, 11, 12],
#[13,14, 15, 0]


    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zero = False        
        first_col_has_zero = False

        # check if the first row contains zero
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break

        # check if the first column contains zero
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break

# first_col_contains_zero = True        

        # use the first row and column as a note
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

#[1,  0,  3,  0],
#[0,  0,  7,  8],
#[0, 10, 11, 12],
#[0,14, 15, 0]

        
        # set the marked rows to zero
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0


#[1, 0,  3, 0],
#[0, 0,  7, 0],
#[0, 0, 11, 0],
#[0, 0, 15, 0]


        # set the marked columns to zero
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
    

#[1, 0,  3, 0],
#[0, 0,  0, 0],
#[0, 0,  0, 0],
#[0, 0,  0, 0]


        # set the first row to zero if needed
        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # set the first column to zero if needed
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0


#[0, 0,  3, 0],
#[0, 0,  0, 0],
#[0, 0,  0, 0],
#[0, 0,  0, 0]

        return matrix
