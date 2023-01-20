"""
Solution of the medium problem
https://leetcode.com/problems/restore-ip-addresses/
"Restore IP Addresses"
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """Return possible valid IP addresses that can be formed.

        >>> Solution().restoreIpAddresses('25525511135')
        ['255.255.11.135', '255.255.111.35']
        >>> Solution().restoreIpAddresses('0000')
        ['0.0.0.0']
        >>> Solution().restoreIpAddresses('101023')
        ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']

        """
        res = []
        n = len(s)
        for i in range(1, 4):
            for j in range(i + 1, min(i + 4, n)):
                for k in range(j + 1, min(j + 4, n)):
                    a = s[:i]
                    b = s[i:j]
                    c = s[j:k]
                    d = s[k:]
                    if a != str(int(a)) or b != str(int(b)) or c != str(int(c)) or d != str(int(d)):
                        continue
                    if int(a) > 255 or int(b) > 255 or int(c) > 255 or int(d) > 255:
                        continue
                    res.append('.'.join([a, b, c, d]))
        return res

