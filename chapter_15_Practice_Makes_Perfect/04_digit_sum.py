def digit_sum(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n /= 10
    return ans