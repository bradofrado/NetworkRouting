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

		def getShortestPath( self, destIndex ):
				self.dest = destIndex
				# TODO: RETURN THE SHORTEST PATH FOR destIndex
				#			 INSTEAD OF THE DUMMY SET OF EDGES BELOW
				#			 IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
				#			 NEED TO USE
				path_edges = []
				total_length = 0
				node = self.network.nodes[self.source]
				edges_left = 3
				while edges_left > 0:
						edge = node.neighbors[2]
						path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
						total_length += edge.length
						node = edge.dest
						edges_left -= 1
				return {'cost':total_length, 'path':path_edges}

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

		def createEmptyDistAndPrev(self):
			dist = {}
			prev = {}
			for node in self.network.nodes:
				dist[node.node_id] = float('inf')
				prev[node.node_id] = None

			return dist, prev

		def computePathWithQueue(self, queue: PriorityQueue, dist, prev, srcIndex):
			dist[srcIndex] = 0
			queue.make_queue(self.network, dist)
			while not queue.empty():
				min = queue.delete_min()
				for edge in min.neighbors:
					node = edge.dest
					newLength = dist[min.node_id] + edge.length
					if newLength < dist[node.node_id]:
						dist[node.node_id] = newLength
						queue.decrease_key(node, newLength)	
						prev[node.node_id] = node

