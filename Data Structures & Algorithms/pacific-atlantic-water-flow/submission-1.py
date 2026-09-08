class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # search cells that can reach pacific and altantic. then find the intersection
        # instead of find a path to ocean. we start from the ocean and reverse the path

        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()
        visited = set()
        def dfs(i, j, visited, preHeight):
            if i < 0 or i >= row or j < 0 or j >= col or (i,j) in visited:
                return
            if heights[i][j] < preHeight:
                return
            
            visited.add((i,j))

            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])

        for c in range(col):
            dfs(0, c, pac, 0)
            dfs(row - 1, c, atl, 0)
        
        for r in range(row):
            dfs(r, 0, pac, 0)
            dfs(r, col - 1, atl, 0)

        result = pac.intersection(atl)
        return list(result)

        