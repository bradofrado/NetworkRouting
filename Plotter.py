from datetime import datetime
import matplotlib.pyplot as plt
from GraphMaker import GraphMaker
from NetworkRoutingSolver import NetworkRoutingSolver

import time as t
import numpy as np

class Plotter:
	def __init__(self, times, data, log = True) -> None:
		if log:
			plt.xscale("log")
		self.log = log
		self.times = times
		self.data = data
		self.m, = plt.plot([], [])
	def plotAll(self, C = 1):
		X = np.arange(1, self.times[-1], 10)
		self.m.set_xdata(X)

		plt.scatter(self.times, self.data)
		Y = X * C
		Y = Y * np.log(X) if self.log else Y * X
		self.m.set_ydata(Y)

		plt.show()
		pass

class NetworkRoutingPlot():
	def __init__(self, times, useHeap = False) -> None:
		self.times = times
		self.useHeap = useHeap
		self.solver = NetworkRoutingSolver()
		self.graphMaker = GraphMaker()
	
	def plotAll(self, C = 1, start = [], log = True):	
		data = self.getTimesData(start)

		plotter = Plotter(self.times, data, log=log)
		plotter.plotAll(C)
	
	def getTimesData(self, data = []):
		s = "heap" if self.useHeap else "array"
		print("Getting times data for " + s)
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
			return self.solver.computeShortestPaths(0, self.useHeap)

heap = False
data = [10, 100, 1000, 10000, 100000, 1000000]
if not heap:
	start = [0, 0.0016008853912353516, 0.03440098762512207, 3.2163129329681395, 513.680054140091, 51282.0512820512820512]
	plotter = NetworkRoutingPlot(data)
	plotter.plotAll(1/19500000, start, log=False)
else:
	start = [0, 0.0017973899841308594, 0.029798460006713868, 0.22775063514709473, 3.467044401168823, 57.642336797714236]
	plotter = NetworkRoutingPlot(data, True)
	plotter.plotAll(1/240000, start)