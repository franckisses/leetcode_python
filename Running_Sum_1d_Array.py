# -*- encoding: utf-8 -*-
'''
FileName :  Running_Sum_1d_Array.py
DateTime :  2020/08/28 11:34:30
Author   :  Gong Yan 
Version  :  1.0
Contact  :  franck_gxu@outlook.com
Desc     :  None

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
'''

# here put the import lib
class Solution:
    def runningSum(self, nums):
        result = []
        for i in range(1,len(nums)+1):
            result.append(sum(nums[:i]))
        print(result)
if __name__ == "__main__":
    a = Solution()
    a.runningSum([1,2,3,4,5])
    
    
 
    