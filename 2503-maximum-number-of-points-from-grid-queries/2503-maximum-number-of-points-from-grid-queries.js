/**
 * @param {number[][]} grid
 * @param {number[]} queries
 * @return {number[]}
 */
var maxPoints = function(grid, queries) {
    const [m, n, k] = [grid.length, grid[0].length, queries.length];
    const res = new Array(k);
    
    // for grid: [val, row col]
    const pq = new PriorityQueue({compare: (a, b) => a[0] - b[0]});
    const visited = new Set();
    pq.enqueue([grid[0][0], 0, 0]);
    visited.add(`${0},${0}`);
    
    // for queries: [val, index]
    const newQueries = [];
    for(let i = 0; i < k; i++){
        newQueries.push([queries[i], i]);
    }
    
    // descending order by value, because we use pop() to get min value in JS, not use shift() to get it.
    newQueries.sort((a, b) => b[0] - a[0]);
    
    let sum = 0;
    const direct = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    while(newQueries.length > 0){
        const [val, index] = newQueries.pop();
        while(pq.size() > 0 && pq.front()[0] < val){
            const [curVal, row, col] = pq.dequeue();
            sum += 1;
            for(const [dr, dc] of direct){
                const [r, c] = [row + dr, col + dc];
                if(r < 0 || c < 0 || r === m || c === n || visited.has(`${r},${c}`))
                    continue;
                visited.add(`${r},${c}`);
                pq.enqueue([grid[r][c], r, c]);
            }
        }
        res[index] = sum;
    }
    
    while(newQueries.length > 0){
        const [val, i] = newQueries.pop();
        res[i] = sum;
    }
    
    return res;
};