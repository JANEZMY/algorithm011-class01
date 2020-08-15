#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += 1
            n &= (n - 1) # 清除最后一个 1
        return res
        
# @lc code=end


#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dic: return -1
        v = self.dic.pop(key) # 移除该 key
        self.dic[key] = v # 再添加该 key，使得重新排序
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False) # 先进先出，删除最先进入的
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n != 0 and (n & (n - 1)) == 0
        
# @lc code=end


#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31
        while n:
            res += (n & 1) << power # 获取最右边的位，并反转位置
            n = n >> 1
            power -= 1
        return res
        
# @lc code=end


#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        exist, no, dic = [], [], {}
        for i in arr1:
            if i in arr2:
                dic[i] = dic.get(i, 0) + 1
            else:
                no += [i]
        no.sort()
        for i in arr2:
            exist += [i] * dic[i]
        return exist + no

# @lc code=end


#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]: # 列表为空 | 不重合，则添加
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1]) # 重合
        return res

# @lc code=end