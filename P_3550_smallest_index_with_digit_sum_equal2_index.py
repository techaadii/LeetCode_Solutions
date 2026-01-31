class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        quotient:int=-1
        remainder= 0
        output:int=0
        for i in range(len(nums)):
            while(quotient !=0):
                denom=10
                quotient=nums[i]//denom
                remainder=nums[i]%denom
                output+=remainder
                nums[i]=nums[i]//10

            if output==i:
                return i
            output=0
            quotient=-1
        return -1