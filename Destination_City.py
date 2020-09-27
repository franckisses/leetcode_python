# -*- encoding: utf-8 -*-
'''
FileName :  Destination_City.py
DateTime :  2020/09/27 15:48:50
Author   :  Gong Yan 
Version  :  1.0
Contact  :  franck_gxu@outlook.com
Desc     :  

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
'''

# here put the import lib

class Solution:
    def destCity(self, paths):
        for index,value in enumerate(paths):
            current = paths[:index] + paths[index+1:]
            first = [i[0] for i in current]
            if value[-1] not in first:
                return  value[-1]   


a = Solution().destCity([["A","Z"]])
print('destination is:',a)
        