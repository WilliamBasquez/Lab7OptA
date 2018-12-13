"""
@author: William E Basquez
@Course: CS 2302
@Assignment: Lab 6, Option A
@Instructor: Diego Aguirre
@T.A: Manoj Saha
@Last modification: Dic 3, 2018
@Using Diego's Graph Structure
"""
import math
class GraphALNode:

    def __init__(self, item, next, weight):
        self.item = item
        self.next = next
        #changed by William Basquez
        self.weight = weight

class GraphAL:

    def __init__(self, initial_num_vertices, is_directed):
        self.adj_list = [None] * initial_num_vertices
        self.is_directed = is_directed

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.adj_list)

    def add_vertex(self):
        self.adj_list.append(None)

        return len(self.adj_list) - 1  # Return new vertex id

    def add_edge(self, src, dest, weight = 1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        #  TODO: What if src already points to dest?
        if self.adj_list[src] is not None and self.adj_list[src].item == dest:
            print("Edge already added!")		
            return

        self.adj_list[src] = GraphALNode(dest, self.adj_list[src], weight)

        if not self.is_directed:
            self.adj_list[dest] = GraphALNode(src, self.adj_list[dest], weight)

    def remove_edge(self, src, dest):
        self.__remove_directed_edge(src, dest)

        if not self.is_directed:
            self.__remove_directed_edge(dest, src)

    def __remove_directed_edge(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        if self.adj_list[src] is None:
            return

        if self.adj_list[src].item == dest:
            self.adj_list[src] = self.adj_list[src].next
        else:
            prev = self.adj_list[src]
            cur = self.adj_list[src].next

            while cur is not None:
                if cur.item == dest:
                    prev.next = cur.next
                    return

                prev = prev.next
                cur = cur.next

    def get_num_vertices(self):
        return len(self.adj_list)

    def get_vertices_reachable_from(self, src):
        reachable_vertices = set()

        temp = self.adj_list[src]

        while temp is not None:
            reachable_vertices.add(temp.item)
            temp = temp.next

        return reachable_vertices

    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if temp.item == dest:
                    vertices.add(i)
                    break

                temp = temp.next

        return vertices

    #function to retrieve the weight between 2 nodes
    def get_weight(self, src, dest):
        temp = self.adj_list[src]
        #print("temp", temp.next.item)

        while temp is not None:
            if temp.item == dest:
                return temp.weight
            temp = temp.next

        return math.inf

    #function to retreive all the in-degrees from every node in a graph
    def get_indegrees_every_vertex(self):
        all_indegrees = [0] * self.get_num_vertices()

        for i in range(len(all_indegrees)):
            i_indegrees = self.get_vertices_reachable_from(i)
            for each in i_indegrees:
                all_indegrees[each]+=1
        
        return all_indegrees