

import math
import random

from CS312Graph import CS312Graph, CS312Point

class GraphMaker:
  def __init__(self):
    SCALE = 1.0
    
    self.data_range = { 'x':[-2*SCALE,2*SCALE], \
                'y':[-SCALE,SCALE] }
  def generateNetwork(self, size, seed = 1):
    random.seed( seed )
    nodes = self.newPoints(size)
    OUT_DEGREE = 3
    size = len(nodes)
    edgeList = {}
    for u in range(size):
      edgeList[u] = []
      pt_u = nodes[u]
      chosen = []
      for i in range(OUT_DEGREE):
        v = random.randint(0,size-1)
        while v in chosen or v == u:
          v = random.randint(0,size-1)
        chosen.append(v)
        pt_v = nodes[v]
        uv_len = math.sqrt( (pt_v.x()-pt_u.x())**2 + \
                  (pt_v.y()-pt_u.y())**2 )
        edgeList[u].append( (v,100.0*uv_len) )
      edgeList[u] = sorted(edgeList[u], key=lambda n:n[0])
    return CS312Graph(nodes, edgeList)
    
    
  def newPoints(self, npoints):
    # TODO - ERROR CHECKING!!!!
    ptlist = []
    RANGE = self.data_range
    xr = self.data_range['x']
    yr = self.data_range['y']
    while len(ptlist) < npoints:
      x = random.uniform(0.0,1.0)
      y = random.uniform(0.0,1.0)
      if True:
        xval = xr[0] + (xr[1]-xr[0])*x
        yval = yr[0] + (yr[1]-yr[0])*y
        ptlist.append( CS312Point(xval,yval) )
    return ptlist