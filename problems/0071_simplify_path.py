"""
Solution of the medium problem
https://leetcode.com/problems/simplify-path/
"Simplify Path"
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        """Return the simplified canonical path.

        >>> Solution().simplifyPath('/home/')
        '/home'
        >>> Solution().simplifyPath('/home//foo/')
        '/home/foo'
        >>> Solution().simplifyPath('/home/user/Documents/../Pictures')
        '/home/user/Pictures'
        >>> Solution().simplifyPath('/../')
        '/'
        >>> Solution().simplifyPath('/.../a/../b/c/../d/./')
        '/.../b/d'

        """
        pathitems = []
        for item in path.split('/'):
            if not item:
                continue
            if item == '.':
                continue
            if item == '..':
                if pathitems:
                    pathitems.pop()
                continue
            pathitems.append(item)

        return '/' + '/'.join(pathitems)

