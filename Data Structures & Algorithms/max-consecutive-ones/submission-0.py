class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #Create Variable 
        count = 0 
        inside_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                inside_count += 1
                if inside_count > count:
                    count = inside_count
            else:
                inside_count = 0
        
        return count
