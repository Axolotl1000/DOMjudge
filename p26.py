def max_a(times: int) -> int:
    if times <= 0:
        return 0
    dp = [0] * (times + 1)
    
    for i in range(1, times + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(1, i - 2):
            total_a = dp[j] * (i - j - 1)
            if total_a > dp[i]:
                dp[i] = total_a
                
    return dp[times]

print(max_a(int(input())))