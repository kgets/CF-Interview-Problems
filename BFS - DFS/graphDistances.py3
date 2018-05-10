def graphDistances(g, s):
    g=Graph(g)
    return g.dijkstra(s)

class Graph():
	def __init__(self, graph):
		self.V = len(graph)
		self.graph = graph

	def minDistance(self, dist, SPT):
		# Initilaize min distance as large int to represent ~INF
		min_ = 1e9
		# Search not nearest vertex not in Shortest Path Tree 
		for v in range(self.V):
			if dist[v]!=-1 and dist[v] < min_ and not SPT[v] :
				min_ = dist[v]
				min_index = v
		return min_index

	# Dijkstra's single source graph algorithm 
	def dijkstra(self, sourceNode):
		print('Dijkstra')
		dist = [1e9] * self.V
		dist[sourceNode] = 0
		SPT = [0] * self.V
		# loop size(v) times to find all vertecies
		for _ in range(self.V):
			print('d:',dist)
			print('spt:',SPT)
			# find closest vertex not in SPT 
			u = self.minDistance(dist, SPT)
			# mark vertex found (vertex in SPT)
			SPT[u] = 1
			# update distance values for adjacent verticies 
			# if (new distance to vertex is less and vertex not in SPT)
			for v in range(self.V):
				if self.graph[u][v] >= 0 and not SPT[v] and dist[v] > dist[u] + self.graph[u][v]:
						dist[v] = dist[u] + self.graph[u][v]
		return dist
