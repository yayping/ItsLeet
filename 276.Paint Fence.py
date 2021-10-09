
"""You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

Every post must be painted exactly one color.
There cannot be three or more consecutive posts with the same color.
Given the two integers n and k, return the number of ways you can paint the fence.

"""


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k * k
        
        for i in range(3, n + 1):
            dp[n] = (k - 1) * (dp[n-1] + dp[n-2])
        
        return dp[n]