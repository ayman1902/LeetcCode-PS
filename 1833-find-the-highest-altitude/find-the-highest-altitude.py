class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitudes=[0]*(len(gain)+1)
        for i in range(1,len(gain)+1):
            altitudes[i]=gain[i-1]+altitudes[i-1]
        max=altitudes[0]
        for i in range(1,len(altitudes)):
            if altitudes[i]>max:
                max=altitudes[i]
        return max