class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        for right in range(1,len(prices)):
            if prices[right] < prices[left]:
                left = right
                right += 1
            elif prices[right] > prices[left]:
                    curr = prices[right] - prices[left]
                    if curr > maxProfit:
                        maxProfit = curr
            
        
        return maxProfit
