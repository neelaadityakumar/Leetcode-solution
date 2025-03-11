var numberOfSubstrings = function(s) {
    let left = 0;
    let right = 0;
    let end = s.length - 1;
    const map = {};

    let count = 0;

    while (right !== s.length) {
        map[s[right]] = (map[s[right]] || 0) + 1;

        while (map['a'] && map['b'] && map['c']) {
            count += 1 + (end - right);
            map[s[left]] -= 1;
            left++;
        }
        right++;
    }
    return count;
};
