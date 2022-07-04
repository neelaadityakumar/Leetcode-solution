class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        t, graph, q = [0] + [float("inf")] * N, collections.defaultdict(list), collections.deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while q:
            time, node = q.popleft()
            if time < t[node]:
                t[node] = time
                for v, w in graph[node]:
                    q.append((time + w, v))
        mx = max(t)
        return mx if mx < float("inf") else -1