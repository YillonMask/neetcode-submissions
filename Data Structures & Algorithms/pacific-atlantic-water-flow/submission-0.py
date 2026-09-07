class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(i, j, visited, preHeight):
            if i < 0 or i >= row or j < 0 or j >= col or heights[i][j] < preHeight:
                return 
            if (i, j) in visited:
                return
            
            visited.add((i,j))
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])

        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row - 1, c, atl, heights[row - 1][c])

        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col - 1, atl, heights[r][col - 1])

        res = []
        for (i, j) in pac:
            if (i, j) in atl:
                res.append([i, j])

        return res