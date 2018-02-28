class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minList = []
        for time in timePoints:
            minute = int(time[:2])*60+int(time[3:])
            minute2 = minute+24*60
            minList.append(minute)
            minList.append(minute2)
        print minList

        minList.sort()
        diff = 1441
        for i in range(1, len(minList)):
            diff = min(diff, minList[i]-minList[i-1])
        return diff

#timeP = ["12:12","12:13","00:12","00:13"]
timeP = ["23:59","00:00"]
s = Solution()
ans = s.findMinDifference(timeP)
print ans