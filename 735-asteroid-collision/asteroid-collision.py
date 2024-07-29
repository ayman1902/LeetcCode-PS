class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for ster in asteroids:
            while stack and stack[-1]>0>ster:
                if abs(ster)>stack[-1]:
                    stack.pop()
                    continue
                elif abs(ster)==stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(ster)
        return stack
        