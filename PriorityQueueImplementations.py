from PriorityQueue import PriorityQueue


class ArrayPriorityQueue(PriorityQueue):
	def __init__(self):
		self.dist = {}
		self.count = 0
		self.keys = set()
		self.map = None
		pass

	def delete_min(self):
		minIndex = -1
		keys = self.keys
		for key in keys:
			if minIndex == -1 or self.dist[key] < self.dist[minIndex]:
				minIndex = key

		if minIndex == -1:
			return None
		
		self.keys.remove(minIndex)
		self.dist.pop(minIndex)
		return minIndex

	def decrease_key(self, key, val):
		self.dist[key] = val

	def empty(self):
		return len(self.keys) == 0

	def make_queue(self, keys, dist, map = lambda x: x):
		self.map = map
		for i in range(len(keys)):
			self.insert(keys[i], dist[i])


	def insert(self, key, val):
		self.dist[key] = val
		key = self.map(key) if self.map != None else key
		self.keys.add(key)

class HeapPriorityQueue(PriorityQueue):
	def __init__(self):
		self.heap = {}
		self.pointer = {}
		self.count = 0
		pass
	def delete_min(self):
		min = self.heap[0][0]
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
		keys = mapKeys(keys, map)
		for i in range(len(keys)):
			key = keys[i]
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