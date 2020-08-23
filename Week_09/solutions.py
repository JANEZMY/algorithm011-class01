#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)   
# @lc code=end


#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])    
# @lc code=end


#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        return sum(s in J for s in S)
# @lc code=end

#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = collections.Counter(s)
        for k, v in enumerate(s):
            if c[v] == 1:
                return k
        return -1
# @lc code=end


#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2147483647    
        INT_MIN = -2147483648
        str = str.lstrip()
        num_re = re.compile(r'^[\+\-]?\d+') # 设置正则规则
        num = num_re.findall(str)
        num = int(*num) # 由于返回的是个列表，解包并且转换成整数
        return max(min(num,INT_MAX),INT_MIN)
# @lc code=end


#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
# @lc code=end

