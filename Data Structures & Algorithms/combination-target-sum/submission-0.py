class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        ans = []

        def backTrack(i, curr, total):
            #Base Case
            if total == target:
                ans.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            

            #Tree Decisions
            curr.append(nums[i])
            backTrack(i, curr, total + nums[i])
            curr.pop()
            backTrack(i+1, curr, total)
        

        backTrack(0, [], 0)
        return ans    