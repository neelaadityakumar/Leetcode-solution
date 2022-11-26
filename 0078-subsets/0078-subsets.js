/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    let res=[[]]
    n=nums.length;
    for(let i=0;i<n;i++ ){
        const prev=[...res];
        for(let j=0;j<res.length;j++){
            res[j]=[...res[j],nums[i]];
            
        }
        res=[...prev,...res]
    }
    return res;
};