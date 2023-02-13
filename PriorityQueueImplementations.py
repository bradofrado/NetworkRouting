from PriorityQueue import PriorityQueue


class ArrayPriorityQueue(PriorityQueue):
	def delete_min(self):
		minIndex = -1
		for node_id in self.dist.keys():
			if self.dist[node_id] != None and (minIndex == -1 or self.dist[node_id] < self.dist[minIndex]):
				minIndex = node_id

		if minIndex == -1:
			return None
		
		self.count -= 1
		self.dist[minIndex] = None
		return self.nodes[minIndex]

	def decrease_key(self, node, val):
		self.dist[node.node_id] = val

	def empty(self):
		return self.count == 0

	def make_queue(self, network, dist):
		self.dist = dist.copy()
		self.count = len(self.dist)
		self.nodes = network.nodes.copy()
		pass

class HeapPriorityQueue(PriorityQueue):
	pass
	# def delete_min(self):
	# 	pass

	# def decrease_key(self, node, val):
	# 	pass

	# def empty(self):
	# 	pass

	# def make_queue(self, network, dist):
	# 	pass