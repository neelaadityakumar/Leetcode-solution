var minimumRecolors = function(blocks, k) {
    let min_count = Number.MAX_VALUE
    for(let i=0; i<blocks.length; i++){
        let black_count = 0, count = 0
        for(let j=i; j<blocks.length; j++){
            if(blocks.charAt(j) == 'B') black_count++
            else{
                black_count++
                count++
            }
            if(black_count == k){
                min_count = Math.min(min_count, count)
                break
            }
        }
    }
    return min_count
};