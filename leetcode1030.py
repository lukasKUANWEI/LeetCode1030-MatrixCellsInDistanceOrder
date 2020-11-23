import collections
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        d=collections.defaultdict(list)
        res=[]
        for i in range(R):
            for j in range(C):
                d[abs(i-r0)+abs(j-c0)].append([i,j])
        #print(d)
        
        maxd=max(d.keys())
        #print(maxd)
        for i in range(maxd+1):
            res+=d[i]
        return res
