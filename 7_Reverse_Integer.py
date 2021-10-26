"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 """
 class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        flag = 1
        if x < 0:
            flag = -1
            x = x*-1
            
        while x > 0:
            if res > (2**31-1)//10:
                return 0
            
            res = res*10 + x%10
            x = x//10
        return res*flag
        