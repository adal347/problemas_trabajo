def depositProfit(deposit, rate, threshold):
    if deposit >= threshold:
        return 0
    else:
        rateAmount = deposit * (rate/100)
        deposit += rateAmount
        return depositProfit(deposit, rate, threshold) + 1
