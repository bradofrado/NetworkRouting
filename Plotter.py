from datetime import datetime
import matplotlib.pyplot as plt
from GraphMaker import GraphMaker
from NetworkRoutingSolver import NetworkRoutingSolver

import time as t
import numpy as np

class Plotter:
	def __init__(self, times, data) -> None:
		plt.xscale("log")
		self.times = times
		self.data = data
		self.m, = plt.plot([], [])
	def plotAll(self, C = 1):
		X = np.arange(1, self.times[-1], 10)
		self.m.set_xdata(X)

		plt.scatter(self.times, self.data)
		self.m.set_ydata(X * np.log(X) * C)

		plt.show()
		pass

class NetworkRoutingPlot():
	def __init__(self, times) -> None:
		self.times = times
		self.solver = NetworkRoutingSolver()
		self.graphMaker = GraphMaker()
	
	def plotAll(self, C = 1, start = []):	
		data = self.getTimesData(start)

		plotter = Plotter(self.times, data)
		plotter.plotAll(C)
	
	def getTimesData(self, data = []):
		if len(data) > 0:
			return data
		mean = lambda arr: np.mean(arr)
		for i in range(len(self.times)):
			time = self.times[i]
			diffs = []
			for j in range(5):
				diff = self.getTimeData(time)
				print("Time for " + str(time) + ": " + str(diff))
				diffs.append(diff)
			print("Mean for " + str(time) + ": " + str(mean(diffs)))
			data.append(mean(diffs))
		return data
	def getTimeData(self, time):
			seed = int(datetime.now().timestamp())
			graph = self.graphMaker.generateNetwork(time, seed)
			self.solver.initializeNetwork(graph)
			return self.solver.computeShortestPaths(0, True)

data = [10, 100, 1000, 10000, 100000]
plotter = NetworkRoutingPlot([1000000])
start = [0.0009983539581298827, 0.006400585174560547, 0.061197757720947266, 0.7401457309722901, 10.25758695602417]
plotter.plotAll(1/113500)