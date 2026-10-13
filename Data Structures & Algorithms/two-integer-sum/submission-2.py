class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        


        #input is a list 
        #output is indexes that meet the requirements 


        indexes = []

        if not nums:
            return indexes

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    if i not in indexes:
                        indexes.append(i)
                    if j not in indexes:
                        indexes.append(j)

        return indexes
