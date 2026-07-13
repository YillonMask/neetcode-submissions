class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check three conditions one by one
        # first check each row 
        row, col = len(board), len(board[0])
        for i in range(row):
            seen = set()
            for j in range(col):
                cur = board[i][j]
                if cur == ".":
                    continue
                cur_num = int(cur)
                if cur_num in seen:
                    return False
                seen.add(cur_num)
        # second check each column
        for i in range(col):
            seen = set()
            for j in range(row):
                cur = board[j][i]
                if cur == ".":
                    continue
                cur_num = int(cur)
                if cur_num in seen:
                    return False
                seen.add(cur_num)
        # last check 3 x 3 sub boxes
        for i in range(0, row, 3):
                for j in range(0, col , 3):
                    seen = set()
                    for m in range(3):
                        for n in range(3):
                            cur = board[i + m][j + n]
                            if cur == ".":
                                continue
                            cur_num = int(cur)
                            if cur_num in seen:
                                return False
                            seen.add(cur_num)
        return True
