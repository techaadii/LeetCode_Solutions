class Solution:
    def searchInsert(self, nums, target: int) -> int:
        min:int=nums[0]

        for i in range(len(nums)):
            if target==nums[i]:
                return i

            else:
                if target<nums[i]:
                    return i
        return i+1