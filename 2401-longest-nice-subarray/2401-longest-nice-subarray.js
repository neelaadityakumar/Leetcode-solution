var longestNiceSubarray = function (nums) {
  let l = 0, bitmask = 0, max = 0;
  for (let r = 0; r < nums.length; r++) {
    while (bitmask & nums[r]) bitmask ^= nums[l++];
    bitmask |= nums[r];
    max = Math.max(max, r - l + 1);
  }
  return max;
};