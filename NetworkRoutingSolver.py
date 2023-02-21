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
			queue.make_queue(self.network.nodes, dist, lambda node: node.node_id)
			while not queue.empty():
				node_id = queue.delete_min()
				min = self.network.nodes[node_id]
				for edge in min.neighbors:
					node = edge.dest
					newLength = dist[min.node_id] + edge.length
					if newLength < dist[node.node_id]:
						dist[node.node_id] = newLength
						queue.decrease_key(node.node_id, newLength)	
						prev[node.node_id] = edge

