from typing import List
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    max_profit=0
    current_stock_price = prices[0]

    for i in range(1,len(prices)):
      selling_price=prices[i]
      max_profit=max(max_profit,selling_price-current_stock_price)
      current_stock_price=min(current_stock_price,prices[i])
    return max_profit
prices = [7,1,5,3,6,4]

obj = Solution()
print(obj.maxProfit(prices))