# https://leetcode.cn/problems/squares-of-a-sorted-array/

# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
from typing import List

# 没有使用双指针的思想
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=[i**2 for i in nums]
        nums.sort()
        return nums

# 使用双指针的思想
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length=len(nums)
        ans=[0]*length
        cur=length-1
        nums=[i**2 for i in nums]
        l,r=0,length-1
        while l<=r:
            if nums[l]>nums[r]:
                ans[cur]=nums[l]
                l+=1
                cur-=1
            else:
                ans[cur]=nums[r]
                r-=1
                cur-=1
        return ans


solution=Solution()
print(solution.sortedSquares([-4,-1,0,3,10]))

solution2=Solution2()
print(solution2.sortedSquares([-4,-1,0,3,10]))