# https://leetcode.cn/problems/remove-element/

'''给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
返回新数组的有效长度'''

from typing import List

# 当前指针为要删除元素则不移动，覆盖该值
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[cur]=nums[i]
                cur+=1
        return cur

solution=Solution()
print(solution.removeElement([3,2,2,3],3))