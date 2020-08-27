# -*- encoding: utf-8 -*-
'''
FileName :  add_two_nums.py
DateTime :  2020/08/27 15:49:53
Author   :  Gong Yan 
Version  :  1.0
Contact  :  yangong1@huawei.com
Des     :

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# here put the import lib
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # frist compare the length of listNode
        a = ListNode()
        result = []
        for i in range(len(l1)):    
            temp = l1[i] + l2[i]
            temp = a.val +temp 
            if temp - 10 >= 0:        # 计算加和是否大于10 
                a.val = 1
                result.append(temp - 10)
            else:
                result.append(temp % 10)
        result.append(a.val)
        return result
if __name__ == "__main__":
    a = Solution()
    l1 = [1,8,9,9]
    l2 = [9,9,9,3]
    a.addTwoNumbers(l1,l2)

