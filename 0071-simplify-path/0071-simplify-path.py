class Solution(object):
    def simplifyPath(self, path):
        stack = []
        directory = path.split('/')
        for dir in directory:
            if dir == '.' or not dir:
                continue
            elif dir == '..':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(dir)
        # if stack[-1] == '/':
        #     stack.pop()
        return '/'+'/'.join(stack)
        
        