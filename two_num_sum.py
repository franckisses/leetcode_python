# -*- encoding: utf-8 -*-
'''
FileName :  two_num_sum.py
DateTime :  2020/08/27 15:19:26
Author   :  Gong Yan 
Version  :  1.0
Contact  :  yangong1@huawei.com
Desc     :  find the first result that is add the two nums.
'''

# here put the import lib
 
class Solution:
    def twoSum(self, nums, target):
        print(nums)
        for i in range(len(nums)-1):
               for j in range(i+1,len(nums)):
                   if nums[i] + nums[j] == target:
                       return [i,j]


if __name__ == "__main__":
    a  = Solution()
    nums = [1,2,3,4,5,6,7]
    target = 4
    result = a.twoSum(nums, target)
    print(result,target)