class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0 for i in range(numCourses)]
        connection = {i:[] for i in range(numCourses)}
        for link in prerequisites:
            connection[link[1]].append(link[0])
            indegree[link[0]] += 1
        zero_indegree = []
        for i in range(numCourses):
            if indegree[i] == 0:
                zero_indegree.append(i)
        i = 0
        while i<len(zero_indegree):
            for node in connection[zero_indegree[i]]:
                indegree[node] -= 1
                if  indegree[node] == 0:
                    zero_indegree.append(node)
            i += 1
        if len(zero_indegree) == numCourses:
            return True
        else:
            return False


solve = Solution()
# print(solve.canFinish(2, [[1, 0], [0, 1]]))
# print(solve.canFinish(2, [[1,4],[2,4],[3,1],[3,2]]))
# print(solve.canFinish(2, [[1, 0]]))
print(solve.canFinish(2, [[0, 1]]))