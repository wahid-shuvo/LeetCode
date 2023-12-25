class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        count = left = right = 0
        good_string = ''

        for right in range(len(s)):
            good_string += s[right]
            if len(good_string) == 3:
                count += 1

            while len(good_string) >= 3:
                good_string = good_string[1:]
                left += 1

        return count


obj = Solution()
obj.countGoodSubstrings('asdfedshdk')
