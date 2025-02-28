
var shortestCommonSupersequence = function (str1, str2) {
//Store DP in t
  let t = new Array(str1.length + 1);
  for (let j = 0; j < t.length; j++) {
    t[j] = new Array(str2.length + 1);
  }
  let m = str1.length;
  let n = str2.length;
// Function to get LCS length
  var longestCommonSubsequence = function (text1, text2) {
    for (let i = 0; i < m + 1; i++) {
      for (let j = 0; j < n + 1; j++) {
        if (i == 0 || j == 0) t[i][j] = 0;
      }
    }

    for (let i = 1; i < m + 1; i++) {
      for (let j = 1; j < n + 1; j++) {
        if (text1[i - 1] === text2[j - 1]) {
          t[i][j] = 1 + t[i - 1][j - 1];
        } else {
          t[i][j] = Math.max(t[i][j - 1], t[i - 1][j]);
        }
      }
    }
    return t[m][n];
  };

  let scsLength = m + n - longestCommonSubsequence(str1, str2);
  let i = m;
  let j = n;
  let s = new Array(scsLength);

//Backtracking if both characters are common in string1  and string 2 input once
  while (i > 0 && j > 0) {
    if (str1[i - 1] === str2[j - 1]) {
      s[scsLength - 1] = str1[i - 1];
      i--;
      j--;
      scsLength--;
    } else if (t[i][j - 1] == t[i][j]) {
      s[scsLength - 1] = str2[j - 1];
      j--;
      scsLength--;
    } else {
      s[scsLength - 1] = str1[i - 1];
      i--;
      scsLength--;
    }
  }

  while (j > 0) {
    s[scsLength - 1] = str2[j - 1];
    j--;
    scsLength--;
  }

  while (i > 0) {
    s[scsLength - 1] = str1[i - 1];
    i--;
    scsLength--;
  }
  return s.join("");
};