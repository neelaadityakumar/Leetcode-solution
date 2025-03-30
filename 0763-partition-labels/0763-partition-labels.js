/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function(s) {
     let lastIndexMap = new Map();
    
    for(let i=0; i < s.length; i++) {
        lastIndexMap.set(s[i], i);
    }
    
    let result = [];
    let size = 0; 
    let end = 0;
    
    for(let j=0; j < s.length; j++) {
        size += 1;
        end = Math.max(end, lastIndexMap.get(s[j]));
        
        if(j==end) {
            result.push(size);
            size = 0;
        }            
    }
    
    return result;
};