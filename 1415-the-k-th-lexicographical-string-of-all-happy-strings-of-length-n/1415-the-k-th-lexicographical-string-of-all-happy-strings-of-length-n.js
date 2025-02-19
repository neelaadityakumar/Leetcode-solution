var getHappyString = function(n, k) {
    let n2 = n;

    function dfs(prefix, n, k) {
        if (n === 0) return prefix;
        for (let c of ['a', 'b', 'c']) {
            if (prefix.length > 0 && c === prefix[prefix.length - 1]) continue;
            let cnt = 2 ** (n2 - prefix.length - 1);
            if (cnt >= k) return dfs(prefix + c, n - 1, k);
            else k -= cnt;
        }
        return "";
    }

    return dfs("", n, k);
};