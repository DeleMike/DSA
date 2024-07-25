def maxProfit(self, prices: List[int]) -> int:
    l = 0
    r = 1
    maxProfit = 0
    while r < len(prices): # make sure it is bounded
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
        else:
            l = r
        r+=1
    return maxProfit

# time complexity = O(n)
# space complexity = O(1)