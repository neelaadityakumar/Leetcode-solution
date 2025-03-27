/**
 * @param {number[]} nums
 * @return {number}
 */

var majorityElement = function (nums) {
    // constraint "nums has exactly one dominant element" given therefore:

    // pass1: find majority element
    let count = 0;
    let ele = nums[0];
    nums.forEach((num) => {
        if (count === 0) {
            ele = num;
        }
        count += ele === num ? 1 : -1;
    });

    // pass2: find freq of majority element
    count = 0;
    nums.forEach((num) => (count += ele === num ? 1 : 0));
    return [ele, count];
};

var minimumIndex = function (nums) {
    let [ele, total] = majorityElement(nums);
    let count = 0;
    // pass3: check if both subarrays meet the condition freq(x) * 2 > m
    for (let i = 0; i < nums.length; i++) {
        if (ele === nums[i]) count++;
        if (count * 2 > i + 1 && (total - count) * 2 > nums.length - (i + 1)) return i;
    }
    return -1;
};