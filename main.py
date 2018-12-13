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
from KruskalsAndTopological import Kruskals, topological_sort

def main():
	graph = GraphAL(5, False)
	graph = GraphAM(5, False)
	Graph = GraphAL(5, True)

	graph.add_edge(0, 1, 3)
	graph.add_edge(0, 2, 5)
	graph.add_edge(1, 3, 4)
	graph.add_edge(1, 4, 2)
	graph.add_edge(2, 3, 9)
	graph.add_edge(2, 4, 7)

	Graph.add_edge(0, 1)
	Graph.add_edge(0, 2)
	Graph.add_edge(1, 4)
	Graph.add_edge(1, 3)
	Graph.add_edge(2, 3)
	Graph.add_edge(4, 2)

	print("Kruskal's Algorithm:")
	if Kruskals(graph, 0) != None:
		for i in Kruskals(graph, 0):
			print(i.item, "-", i.next, "; weight:",i.weight)

	print("\nTopological Sort:")
	print(topological_sort(Graph))

main()
"""
Sources
https://www.cs.usfca.edu/~galles/visualization/TopoSortIndegree.html
https://www.cs.usfca.edu/~galles/visualization/Kruskal.html
https://brilliant.org/wiki/sorting-algorithms/
"""