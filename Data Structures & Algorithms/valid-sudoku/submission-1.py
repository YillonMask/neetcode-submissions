class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #one pass, using hashsets for each row, col and 3*3 square
        # row : number, col : number, (sqr_row, sqr_col) : number
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        sqr_dict = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in row_dict[row] or
                board[row][col] in col_dict[col] or
                board[row][col] in sqr_dict[(row // 3, col // 3)]):
                    return False

                row_dict[row].add(board[row][col])
                col_dict[col].add(board[row][col])
                sqr_dict[(row // 3, col // 3)].add(board[row][col])
        return True