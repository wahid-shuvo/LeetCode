class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:

    bucket=set()
    left=0
    right=0
    max_length=0
    while(right<len(s)):
      length = (right - left) + 1
      if max_length<length:
        max_length=length

      if s[right] not in bucket:
        bucket.add(s[right])
        right=right+1
      else:
        bucket.remove(s[left])
        left=left+1

    # max_length = 0
    # if(len(s))==1:
    #   return 1
    # for i in range(len(s)):
    #   substring = []
    #   substring.append(s[i])
    #   for j in range(i+1,len(s)):
    #     if s[j] not in substring:
    #       substring.append(s[j])
    #     else:
    #       substring=[]
    #       substring.append(s[j])
    #     if len(substring) > max_length:
    #       max_length = len(substring)
    return max_length


s = "abcaabcd"
obj=Solution()
print(obj.lengthOfLongestSubstring(s))