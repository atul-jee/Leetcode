class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)*-1
        i=-1
        while i>=n:
            s=digits[i]+1
            rem=s//10
            if rem==0:
                digits[i]+=1
                return digits
            else:
                digits[i]=s%10
            i-=1
        return [1]+digits

            
            
        