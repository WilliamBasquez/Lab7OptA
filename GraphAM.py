"""
@author: William E Basquez
@Course: CS 2302
@Assignment: Lab 6, Option A
@Instructor: Diego Aguirre
@T.A: Manoj Saha
@Last modification: Dic 3, 2018
@Using Diego's Graph structure
"""
class GraphAM:

    def __init__(self, initial_num_vertices, is_directed):
        self.adj_matrix = []

        for i in range(initial_num_vertices):  # Assumption / Design Decision: 0 represents non-existing edge
            self.adj_matrix.append([0] * initial_num_vertices)

        self.is_directed = is_directed

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.adj_matrix)

    def add_vertex(self):
        for lst in self.adj_matrix:
            lst.append(0)

        new_row = [0] * (len(self.adj_matrix) + 1)  # Assumption / Design Decision: 0 represents non-existing edge
        self.adj_matrix.append(new_row)

        return len(self.adj_matrix) - 1  # Return new vertex id

    def add_edge(self, src, dest, weight = 1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.adj_matrix[src][dest] = weight

        if not self.is_directed:
            self.adj_matrix[dest][src] = weight

    def remove_edge(self, src, dest):
        self.add_edge(src,dest, 0)

    def get_num_vertices(self):
        return len(self.adj_matrix)

    def get_vertices_reachable_from(self, src):
        reachable_vertices = set()

        for i in range(len(self.adj_matrix)):
            if self.adj_matrix[src][i] != 0:
                reachable_vertices.add(i)

        return reachable_vertices

    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.adj_matrix)):
            if self.adj_matrix[i][dest] != 0:
                vertices.add(i)

        return vertices

    #function to retrieve the weight between 2 nodes
    def get_weight(self, src, dest):
        if self.is_valid_vertex(src) and self.is_valid_vertex(dest):
            return self.adj_matrix[src][dest]
        return math.inf

    #function to retreive all the in-degrees from every node in a graph
    def get_indegrees_every_vertex(self):
        all_indegrees = [0] * self.get_num_vertices()

        for i in range(len(all_indegrees)):
            i_indegrees = self.get_vertices_reachable_from(i)
            for each in i_indegrees:
                all_indegrees[each]+=1
        
        return all_indegrees
