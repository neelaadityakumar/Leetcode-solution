class Solution:
    def topSort(self, edge_list):
        top_sort = []

        # # create an adjacency list from the edge list given
        # while doing so, create an indegree record for each vertex/node
        adjacency_list = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for arr in edge_list:
            child, parent = arr[0], arr[1]

            adjacency_list[parent].append(child)
            indegrees[child] += 1

        # # add all the sources into a queue
        sources = []
        for vertex in adjacency_list:
            if indegrees[vertex] == 0:
                sources.append(vertex)

        # # build top_sort list
        while sources:
            vertex = sources.pop(0)
            top_sort.append(vertex)
            for child in adjacency_list[vertex]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    sources.append(child)

        # if len(top_sort) == len(adjacency_list), it means the graph is acyclic
        return len(top_sort) == len(adjacency_list)

    def canFinish(self, numCourses, prerequisites):
        return self.topSort(prerequisites)