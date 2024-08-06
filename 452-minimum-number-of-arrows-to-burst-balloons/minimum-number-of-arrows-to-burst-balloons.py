class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        print(points)
        points.sort(key=lambda x:x[1])
        print(points)
        end=points[0][1]
        res=1
        for i in range(1,len(points)):
            if points[i][0]>end:
                res+=1
                end=points[i][1]
            else:
                end=min(end,points[i][1])
        return res

