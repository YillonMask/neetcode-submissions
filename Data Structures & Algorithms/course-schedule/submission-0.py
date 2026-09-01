class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build the graph using dictionary
        adj = defaultdict(list)

        for course, pre in prerequisites:
            adj[course].append(pre)
        
        finished = set()
        visited = set()
        def dfs(course):
            if course in finished:
                return True
            if course in visited:
                return False
            
            visited.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            finished.add(course)
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
