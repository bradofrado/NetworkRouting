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
		self.nodes = network.nodes
		pass

class HeapPriorityQueue(PriorityQueue):
	def delete_min(self):
		min = self.nodes[self.heap[0][0]]
		self.pointer[self.heap[0][0]] = None
		self.heap[0] = None
		self.switch(0, self.count - 1)
		self.count -= 1
		self.delete(0)
		return min

	def delete(self, index):
		if index * 2 + 1 >= self.count:
			return

		left = self.heap[index * 2 + 1]
		right = self.heap[index * 2 + 2] if self.count > index * 2 + 2 else None

		switchIndex = -1
		if right == None or left[1] < right[1]:
			switchIndex = index * 2 + 1
		elif right[1] < left[1]:
			switchIndex = index * 2 + 2	

		if switchIndex != -1 and self.heap[index][1] > self.heap[switchIndex][1]:
			self.switch(index, switchIndex)
			self.delete(switchIndex)

	def switch(self, src, dest):
		srcKey = self.heap[src]
		destKey = self.heap[dest]
		self.heap[src] = destKey
		self.heap[dest] = srcKey
		if srcKey != None:
			self.pointer[srcKey[0]] = dest
		if destKey != None:
			self.pointer[destKey[0]] = src

	def decrease_key(self, node, val):
		index = self.pointer[node.node_id]
		if index == None:
			return

		self.heap[index][1] = val
		self.decrease(index)
	
	def decrease(self, index):
		parentKey = self.heap[index // 2] if index > 0 else None
		if parentKey == None:
			return

		curr = self.heap[index]

		if curr[1] < parentKey[1]:
			self.heap[index // 2] = curr
			self.heap[index] = parentKey
			self.pointer[parentKey[0]] = index
			self.pointer[curr[0]] = index // 2
			self.decrease(index // 2)

	def empty(self):
		return self.count == 0

	def make_queue(self, network, dist):
		self.heap = {}
		self.pointer = {}
		self.nodes = network.nodes
		self.count = len(self.nodes)
		for i in range(len(self.nodes)):
			node = self.nodes[i]
			self.heap[i] = [node.node_id, dist[node.node_id]]
			self.pointer[node.node_id] = i

			if dist[node.node_id] != float('inf'):
				temp = self.heap[0]
				self.heap[0] = self.heap[i]
				self.heap[i] = temp
				self.pointer[node.node_id] = 0
				self.pointer[temp[0]] = i
		pass