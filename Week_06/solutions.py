#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 
        dp = [0] + [float('inf')] * (n - 1)
        for i in range(m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[-1]
# @lc code=end


#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        dp = [1, 1] + [0] * (len(s) - 1)
        for i in range(2, len(s) + 1):
            if 0 < int(s[i - 1: i]): dp[i] = dp[i - 1]
            if 10 <= int(s[i - 2: i]) <= 26: dp[i] += dp[i - 2]
        return dp[-1]
# @lc code=end