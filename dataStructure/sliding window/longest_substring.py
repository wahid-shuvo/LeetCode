def long_substring_one_zero(s):
    left = current = ans = 0

    for right in range(len(s)):
        if s[right] == '0':
            current += 1
        while current > 1:
            if s[left] == '0':
                current -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans


ans=long_substring_one_zero("1101100111")
print(ans)