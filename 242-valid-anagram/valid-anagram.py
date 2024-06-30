class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char=[0]*26
        for a in s:
            char[ord(a)-ord('a')]+=1
        for a in t:
            char[ord(a)-ord('a')]-=1
        for ele in char:
            if ele!=0:
                return False
        return True
