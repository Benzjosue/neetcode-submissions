class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #loop through the array 
        #create an empty dictionary 

        # counts = {}

        # for i in range(len(nums)):
        #     if nums[i] in counts:
        #         return True
        #     else:
        #         counts[nums[i]] = 1

        # return False


        # duplicate = 0 

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False


        seen = []

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.append(nums[i])
        return False



