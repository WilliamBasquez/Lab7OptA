"""
@author: William E Basquez
@Course: CS 2302
@Assignment: Lab 6, Option A
@Instructor: Diego Aguirre
@T.A: Manoj Saha
@Last modification: Dic 3, 2018
"""

from queue import Queue
from GraphAL import GraphAL, GraphALNode
from GraphAM import GraphAM

"""
Using Diego's implemetation of disjoint set forest
"""
class dsf:
    def __init__(self, n):
        self.forest = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index <= len(self.forest)

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.forest[a] < 0:
            return a

        self.forest[a] = self.find(self.forest[a])

        return self.forest[a]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:
            self.forest[rb] = ra

"""
Using insertion sort
"""
def set_sorting(s):
	copy_set = []

	for i in s:
		copy_set.append(i)

	for i in range(1, len(copy_set)):
		temp = copy_set[i]
		j = i-1
		while j >= 0 and temp.weight < copy_set[j].weight:
			copy_set[j+1] = copy_set[j]
			j -= 1
		copy_set[j+1] = temp

	return copy_set

"""
This functions stores all the possible edges between vertices(if there is one)
Then, after sorting those combinations by cost, it unites those combinations
while making sure that a cycle does not occur, at the end the minimum spanning tree
"""
def Kruskals(graph, src):
	if not graph.is_valid_vertex(src):
		return
	visited_vertix = [False] * graph.get_num_vertices()
	combinations = set()
	stack = []
	stack.append(src)

	while len(stack) > 0:
		
		i = stack.pop()
		visited_vertix[i] = True

		for vertex in graph.get_vertices_reachable_from(i):
			if not visited_vertix[vertex]:
				visited_vertix[i] = True
				combinations.add(GraphALNode(i, vertex, graph.get_weight(i, vertex)))
				stack.append(vertex)
	
	copied_set = set_sorting(combinations)
	forest = dsf(len(copied_set))
	returnee = set()
	
	for each in copied_set:
		if forest.find(each.item) != forest.find(each.next):
			forest.union(each.item, each.next)
			returnee.add(each)

	return returnee


"""
Following Topological sort handout
This function orders the vertices from a directed graph
in a way that if there is an edge from u to v, 
u appears before than v
"""
def topological_sort(graph):
	all_in_degrees = graph.get_indegrees_every_vertex()
	sort_result = []

	q = Queue()

	for i in range(len(all_in_degrees)):
		if all_in_degrees[i] == 0:
			q.put(i)

	while not q.empty():
		u = q.get()

		sort_result.append(u)

		for adj_vertex in graph.get_vertices_reachable_from(u):
			all_in_degrees[adj_vertex] -= 1

			if all_in_degrees[adj_vertex] == 0:
				q.put(adj_vertex)

	if len(sort_result) != graph.get_num_vertices():
		return None

	return sort_result