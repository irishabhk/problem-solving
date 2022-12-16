# https://leetcode.com/problems/best-time-to-buy-and-sell-st6
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

def MaxProfit(prices,max,profit):
    for i in range(0,(len(prices)-1)):
        profit=profit+prices[i+1]-prices[i]
        if (profit < 0):
            profit = 0
        if (profit >= max):
            max = profit
    return max 
input = [7,1,5,3,6,4]
output = MaxProfit(input,0,0)
print(output)          


