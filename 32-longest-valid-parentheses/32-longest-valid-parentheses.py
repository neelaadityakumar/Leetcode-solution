class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, curr_longest, max_longest = [], 0, 0
        for c in s:
            if c == '(':
                stack.append(curr_longest)
                curr_longest = 0
            elif c == ')':
                if stack:
                    curr_longest += stack.pop() + 2
                    max_longest = max(max_longest, curr_longest)
                else:
                    curr_longest = 0
        return max_longest