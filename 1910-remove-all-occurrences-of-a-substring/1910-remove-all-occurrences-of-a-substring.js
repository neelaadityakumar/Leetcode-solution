var removeOccurrences = function(s, part) {
    // Build KMP table (LPS array)
    function buildLPS(pattern) {
        let lps = Array(pattern.length).fill(0);
        let len = 0, i = 1;

        while (i < pattern.length) {
            if (pattern[i] === pattern[len]) {
                lps[i++] = ++len;
            } else if (len > 0) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }
        return lps;
    }

    // KMP search function
    function kmpSearch(text, pattern, lps) {
        let i = 0, j = 0;
        while (i < text.length) {
            if (text[i] === pattern[j]) {
                i++;
                j++;
                if (j === pattern.length) return i - j; // Found occurrence
            } else if (j > 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
        return -1; // No occurrence found
    }

    // Main removal process
    let lps = buildLPS(part);
    let index=0
    while (index !== -1) {
        index = kmpSearch(s, part, lps);
        if (index === -1) return s; // No more occurrences
        s = s.slice(0, index) + s.slice(index + part.length);
    }

    return s;
};
