# -*- encoding: utf-8 -*-
'''
FileName :  Kids_With_candy.py
DateTime :  2020/09/27 15:37:22
Author   :  Gong Yan 
Version  :  1.0
Contact  :  franck_gxu@outlook.com
Desc     :  None
'''

# here put the import lib
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result =[]  
        for i in candies:
            if i+extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result
        
a = Solution().kidsWithCandies([1,2,3,4,5,100,6],10)
print(a)
        
