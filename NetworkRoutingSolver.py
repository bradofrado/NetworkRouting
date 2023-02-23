#!/usr/bin/python3


from CS312Graph import *
import time

from PriorityQueue import PriorityQueue
from PriorityQueueImplementations import ArrayPriorityQueue, HeapPriorityQueue


class NetworkRoutingSolver:
		def __init__( self):
				pass

		def initializeNetwork( self, network ):
				assert( type(network) == CS312Graph )
				self.network = network

		# Time: The complexity is that of the while loop which is going to loop through at most each of the 
		#       nodes in prev, which is of length V, so O(V)
		# Space: The space is that of prev which is all the nodes in the graph, or O(V)
		def getShortestPath( self, destIndex ):
				path_edges = []
				total_length = 0
				edge = self.prev[destIndex]

				if edge == None:
					return { 'cost': float('inf'), 'path': [] }

				while edge != None:
					path_edges.append((edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)))
					total_length += edge.length
					edge = self.prev[edge.src.node_id]

				return {'cost':total_length, 'path':path_edges}

		# Time: The complexity is the time for self.createEmptyDistAndPrev or O(V) 
		#       plus the time for computePathWithQueue, which is O(VlogV) for heap and O(V^2) for array
		#       Overall -> Heap: O(VlogV), Array: O(V^2)
		def computeShortestPaths( self, srcIndex, use_heap=False ):
				self.source = srcIndex
				t1 = time.time()
				queue: PriorityQueue = HeapPriorityQueue() if use_heap else ArrayPriorityQueue()
				dist, prev = self.createEmptyDistAndPrev()

				self.computePathWithQueue(queue, dist, prev, srcIndex)
				self.dist = dist
				self.prev = prev

				t2 = time.time()
				return (t2-t1)

		# Time: the time complexity is the amount of nodes, or O(V)
		# Space: the space complexity is the graph stored in self.network.nodes or O(V + E) or O(V)
		#         (since E is proportional to V with 3 edges each node)
		def createEmptyDistAndPrev(self):
			dist = {}
			prev = {}
			for node in self.network.nodes:
				dist[node.node_id] = float('inf')
				prev[node.node_id] = None

			return dist, prev


		# Time: The time complexity is the complexity of the while loop (O(V * delete_min + E*insert)) + 
		# 		  the complexity of the first insert statement, which is constant time because it is only one node
		# 			so an overall of O(V*delete_min + E*insert)
		#   Heap: insert = O(logV)
		#         delete_min = O(logV)
		#         overall = O(V*logV + E*logV)
		#   Array: insert = O(1)
		#          delete_min = O(V)
		#          overall = O(V + EV)
		#       Since E = 3 for each node, it is equivalent to O(V) ->
		#               Overall final answer: Heap -> O(V*logV)
		#                                     Array -> O(V^2)
		# Space: The space complexity is the space of the queue + dist + prev.
		# 			 Dist is all the nodes (O(V)) and the queue never gets more than all the nodes (O(V)). 
		#				 So overall O(V) 
		def computePathWithQueue(self, queue: PriorityQueue, dist, prev, srcIndex):
			dist[srcIndex] = 0
			start = self.network.nodes[srcIndex].node_id
			queue.insert(start, dist[start])
			
			# Looping at most through each node, so V times
			while not queue.empty():
				node_id = queue.delete_min()
				min = self.network.nodes[node_id]
				# Looping through at most each edge, so E times
				for edge in min.neighbors:
					node = edge.dest
					newLength = dist[min.node_id] + edge.length
					if newLength < dist[node.node_id]:
						dist[node.node_id] = newLength
						queue.insert(node.node_id, newLength)
						prev[node.node_id] = edge

