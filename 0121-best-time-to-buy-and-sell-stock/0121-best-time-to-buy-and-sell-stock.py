class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        b = prices[0]
        c_profit = 0
        
        
        for s in prices[1:]:
            if s < b:
                b = s
            else:
                c_profit = max(c_profit, s - b)
                
        return c_profit
        