from PriorityQueue import PriorityQueue


class ArrayPriorityQueue(PriorityQueue):
	def delete_min(self):
		minIndex = -1
		for key in self.dist.keys():
			if self.dist[key] != None and (minIndex == -1 or self.dist[key] < self.dist[minIndex]):
				minIndex = key

		if minIndex == -1:
			return None
		
		self.count -= 1
		self.dist[minIndex] = None
		return self.keys[minIndex]

	def decrease_key(self, key, val):
		self.dist[key] = val

	def empty(self):
		return self.count == 0

	def make_queue(self, keys, dist, map = lambda x: x):
		self.dist = {}
		self.count = 0
		self.keys = []
		self.map = map

		for i in range(len(keys)):
			self.insert(keys[i], dist[i])
		pass

	def insert(self, key, val):
		self.dist[self.count] = val
		self.keys.append(mapKeys([key], self.map)[0])
		self.count += 1

class HeapPriorityQueue(PriorityQueue):
	def delete_min(self):
		min = self.keys[self.heap[0][0]]
		self.pointer[self.heap[0][0]] = None
		self.heap[0] = None
		self.switch(0, self.count - 1)
		self.count -= 1
		self.pDown(0)
		return min

	def decrease_key(self, key, val):
		index = self.pointer[key]
		if index == None:
			return

		self.heap[index][1] = val
		self.pUp(index)

	def empty(self):
		return self.count == 0

	def make_queue(self, keys, dist, map = lambda x: x):
		self.heap = {}
		self.pointer = {}
		self.keys = mapKeys(keys, map)
		self.count = 0
		for i in range(len(self.keys)):
			key = self.keys[i]
			self.insert(key, dist[key])

	def insert(self, key, val):
		i = self.count
		self.heap[i] = [key, val]
		self.pointer[key] = i

		self.pUp(i)
		self.count += 1

	def pUp(self, index):
		parentKey = self.heap[index // 2] if index > 0 else None
		if parentKey == None:
			return

		curr = self.heap[index]

		if curr[1] < parentKey[1]:
			self.switch(index, index // 2)
			self.pUp(index // 2)

	def pDown(self, index):
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
			self.pDown(switchIndex)

	def switch(self, src, dest):
		srcKey = self.heap[src]
		destKey = self.heap[dest]
		self.heap[src] = destKey
		self.heap[dest] = srcKey
		if srcKey != None:
			self.pointer[srcKey[0]] = dest
		if destKey != None:
			self.pointer[destKey[0]] = src

def mapKeys(keys, map):
	out = []
	for key in keys:
		out.append(map(key))

	return out