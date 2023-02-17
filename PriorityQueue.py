import abc

from CS312Graph import CS312Graph, CS312GraphNode

class PriorityQueue(abc.ABC):
	@abc.abstractclassmethod
	def delete_min() -> CS312GraphNode:
		pass

	@abc.abstractclassmethod
	def decrease_key(node: CS312GraphNode, val) -> None:
		pass

	@abc.abstractclassmethod
	def empty() -> bool:
		pass

	@abc.abstractclassmethod
	def make_queue(nodes: CS312Graph, dist, map) -> None:
		pass

	@abc.abstractclassmethod
	def insert(key, val) -> None:
		pass




