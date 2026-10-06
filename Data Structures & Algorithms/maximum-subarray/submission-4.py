class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSub = nums[0]

        for i in nums:
            if sum < 0:
                sum = 0
            sum += i
            maxSub = max(maxSub, sum)
            
        return maxSub
            
