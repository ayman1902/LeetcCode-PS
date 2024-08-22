class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        hashmap=defaultdict(int)
        for i in range(len(sentence)):
            hashmap[sentence[i]]+=1
        return len(hashmap)==26