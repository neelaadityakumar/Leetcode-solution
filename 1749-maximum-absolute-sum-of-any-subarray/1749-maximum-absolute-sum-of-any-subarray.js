
var maxAbsoluteSum = function(nums) {
   let maxSum = Number.MIN_SAFE_INTEGER;
let curMax = 0, curMin = 0;
for (let num of nums) {
    curMax = Math.max(curMax + num, num);
    curMin = Math.min(curMin + num, num);
    maxSum = Math.max(maxSum, curMax, -curMin);
}
return maxSum;

};