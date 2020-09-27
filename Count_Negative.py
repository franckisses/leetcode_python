# -*- encoding: utf-8 -*-
'''
FileName :  Count_Negative.py
DateTime :  2020/09/27 15:23:39
Author   :  Gong Yan 
Version  :  1.0
Contact  :  franck_gxu@oultook.com
Desc     :  None
'''
# here put the import lib



class Solution:
    def countNegatives(self, grid):
        result = 0
        for i in grid:
            for j in i:
                if j < 0:
                    result += 1
        return result

a = Solution()
b = a.countNegatives([[1,-2,3,-1],[3,1,3,-3],[12,-3,1,-1],[1,-4,-1,2]])
print(b)
   