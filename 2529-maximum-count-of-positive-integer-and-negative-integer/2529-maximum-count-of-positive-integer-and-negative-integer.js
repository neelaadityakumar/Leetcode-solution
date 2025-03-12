/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumCount = function (nums) {
    return Math.max(...nums.reduce(([pos, neg], curr) => {
        if (curr > 0) {
            pos++;
        } else if (curr < 0) {
            neg++;
        }
        return [pos, neg]; 
    }, [0, 0]));
};
