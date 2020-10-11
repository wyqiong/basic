# i负责指向不含重复元素序列的最后一个元素
# j负责指向未进行决策的序列的首个元素

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        
        for _ in range(len(nums)):
            if not nums[i]==nums[j]:
                i = i+1
                nums[i] = nums[j]
            j=j+1
        
        return i+1