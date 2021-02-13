"""
Solution of "Count and Say" problem at
https://leetcode.com/problems/count-and-say/
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        s, pos, cnts = self.countAndSay(n - 1), 0, {}

        for i, c in enumerate(s):
            if (c, pos) not in cnts:
                cnts[c, i] = 0
                pos = i
            cnts[c, pos] += 1

        return ''.join(str(cnts[c, pos]) + c for c, pos in cnts)

