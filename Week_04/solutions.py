#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [l, r]，区间闭合
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2      
            if nums[m] > nums[r]:
                l = m + 1
            else:
                # nums[m] <= nums[r]，因此m可能是最小的
                r = m
        return nums[l]

# @lc code=end


#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

# @lc code=end


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]: return m
            if nums[l] <= nums[m]: # 等号位置
                if nums[l] <= target < nums[m]:
                    r = m - 1 # 已判断m不是
                else:
                    l = m + 1 # 已判断m不是
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1