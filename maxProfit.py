from typing import List
import sys
def maxProfit(prices: List[int]) -> int:
        
    lowest = sys.maxsize
    profit = 0

    for eachPrice in prices:
        lowest = min(lowest,eachPrice)

        currProfit = eachPrice - lowest

        profit = max(currProfit,profit)

    return profit


