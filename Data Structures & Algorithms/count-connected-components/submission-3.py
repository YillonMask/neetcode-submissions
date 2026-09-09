class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = set()
        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
        

        visited = set()
        cnt = 0
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            return
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt += 1
        
        return cnt