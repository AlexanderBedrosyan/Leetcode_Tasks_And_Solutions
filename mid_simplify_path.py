# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file
# system, convert it to the simplified canonical path.
#
# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory
# up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any
# other format of periods such as '...' are treated as file/directory names.

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        components = path.split('/')
        stack = []

        for component in components:
            if component == '..':
                if stack:
                    stack.pop()
            elif component and component != '.':
                stack.append(component)

        return '/' + '/'.join(stack)


solve = Solution()
print(solve.simplifyPath('/home/'))
print(solve.simplifyPath("/home//foo/"))
print(solve.simplifyPath("/../"))