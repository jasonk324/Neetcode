class Solution(object):
    def isValidSudoku(self, board):
        # Checking Each Row
        for row in board:
            row_set = set()
            for item in row:
                if (item in row_set and item != "."):
                    print("IM DOING WOOOO")
                    return False
                else:
                    if item != ".":
                        row_set.add(item)

        # Checking Each Column 
        for c in range(0, len(board)):
            col_set = set()
            for r in range(0, len(board)):
                item = board[r][c] 
                if (item in col_set and item != "."):
                    print("IM DOING THIS")
                    return False
                else:
                    col_set.add(item)

        # Checking Each Sub-Box
        for main_r in range(0, len(board), 3):
            for main_c in range(0, len(board), 3):
                sub_set = set() 
                for r in range(0, 3):
                    for c in range(0, 3):
                        row = main_r + r
                        col = main_c + c
                        item = board[row][col]
                        if (item in sub_set and item != "."):
                            return False
                        else:
                            sub_set.add(item)


        return True

        """
        :type board: List[List[str]]
        :rtype: bool
        """
        