
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word
        if len(self.board):
            self.m, self.n = len(board), len(board[0])
            visited = [[False for _j in range(self.n)] for _i in range(self.m)]
            for i in range(self.m):
                for j in range(self.n):                    
                    if self.dfs(i, j, visited):
                        return True
        return False

    def dfs(self, i, j, visited, depth=0):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            return False

        if visited[i][j]:
            return False
        
        visited[i][j], ret_val = True, False
        if self.board[i][j] == self.word[depth]:
            if depth == len(self.word) - 1:
                return True
            ret_val = ret_val or self.dfs(i - 1, j, visited, depth + 1)
            ret_val = ret_val or self.dfs(i + 1, j, visited, depth + 1)
            ret_val = ret_val or self.dfs(i, j - 1, visited, depth + 1)
            ret_val = ret_val or self.dfs(i, j + 1, visited, depth + 1)
        visited[i][j] = False
        return ret_val
