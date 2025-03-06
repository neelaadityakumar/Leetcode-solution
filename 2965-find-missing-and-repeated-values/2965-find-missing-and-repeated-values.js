function findMissingAndRepeatedValues(grid) {
    const n = grid.length;
    const count = Array(n * n + 1).fill(0); // To store the count of each number
    
    let repeated = 0;
    let missing = 0;
    
    // Count occurrences of each number in the grid
    for (const row of grid) {
        for (const num of row) {
            count[num]++;
            if (count[num] === 2) { // Identify the repeated value
                repeated = num;
            }
        }
    }
    
    // Find the missing value
    for (let i = 1; i <= n * n; ++i) {
        if (count[i] === 0) { // Identify the missing value
            missing = i;
            break;
        }
    }
    
    return [repeated, missing];
}

