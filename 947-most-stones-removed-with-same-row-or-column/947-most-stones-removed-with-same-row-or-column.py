class UnionFind:
	def __init__(self, n):
		self.root = list(range(n))

	def union(self, x, y):
		self.root[self.find(x)] = self.find(y)

	def find(self, x):
		if x != self.root[x]:
			self.root[x] = self.find(self.root[x])
		return self.root[x]

	def num_components(self):
		x = set([])
		for i in range(len(self.root)):
			x.add(self.find(i))
		return len(x)

class Solution:
	def removeStones(self, stones: List[List[int]]) -> int:
		uf = UnionFind(len(stones))

		col_prev = {}
		row_prev = {}
		for i, (x, y) in enumerate(stones):
			if x in row_prev:
				uf.union(i, row_prev[x])
			if y in col_prev:
				uf.union(i, col_prev[y])
			row_prev[x] = i
			col_prev[y] = i

		return len(stones) - uf.num_components()