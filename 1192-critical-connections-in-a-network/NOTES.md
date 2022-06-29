we recursively call dfs on each of the unvisited adjacent nodes (next) of the current node (curr). If one of the possible next nodes is an earlier node (disc[next] < curr[low]), then we've found a loop and we should update the low value for the current node. As each layer of the recursive function backtracks, it will propagate this value of low back down the chain.
​
If, after backtracking, the value of low[next] is still higher than disc[curr], then there is no looped connection, meaning that the edge between curr and next is a bridge, so we should add it to our answer array (ans).
​
​