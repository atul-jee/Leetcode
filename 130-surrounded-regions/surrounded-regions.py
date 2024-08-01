from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m = len(board)
        n = len(board[0])
        
        def dfs(mat, i, j, m, n):
            if i < 0 or i >= m or j < 0 or j >= n or mat[i][j] != 'O':
                return 
            mat[i][j] = '#'  # Mark as visited
            dfs(mat, i + 1, j, m, n)
            dfs(mat, i - 1, j, m, n)
            dfs(mat, i, j + 1, m, n)
            dfs(mat, i, j - 1, m, n)

        # Perform DFS for 'O's on the boundary
        for i in range(m):
            if board[i][0] == 'O':
                dfs(board, i, 0, m, n)
            if board[i][n - 1] == 'O':
                dfs(board, i, n - 1, m, n)
                
        for j in range(n):
            if board[0][j] == 'O':
                dfs(board, 0, j, m, n)
            if board[m - 1][j] == 'O':
                dfs(board, m - 1, j, m, n)

        # Replace all remaining 'O's with 'X' and '#' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
