class Solution:
    def romanToInt(self, s: str) -> int:

        left=0
        right=0
        integer=0

        map={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        while left<len(s):
            if left<len(s)-1:
                if s[left]=="I" and (s[left+1]=="V" or s[left+1]=="X"):
                    integer+=map[s[left+1]]-1
                    left=left+2
                elif s[left]=="X" and (s[left+1]=="L" or s[left+1]=="C"):
                    integer+=map[s[left+1]]-10
                    left=left+2
                elif s[left]=="C" and (s[left+1]=="D" or s[left+1]=="M"):
                    integer+=map[s[left+1]]-100
                    left=left+2
                else:
                    integer += map[s[left]]
                    left += 1
            else:
                integer+=map[s[left]]
                left+=1
        return integer

obj=Solution()
s = "MCMXCIV"
obj.romanToInt(s)


