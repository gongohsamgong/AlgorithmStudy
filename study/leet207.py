class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = set()
        traced = set()

        def dfs(x):
            if x in traced:
                return False
            if x in visited:
                return True

            traced.add(x)
            for y in graph[x]:
                if not dfs(y):
                    return False
            traced.remove(x)
            visited.add(x)

            return True

        for n in list(graph):
            if not dfs(n):
                return False
        return True
    