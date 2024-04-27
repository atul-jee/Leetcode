class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for i in range(n-1,-1,-1):
            s=digits[i]+1
            rem=s//10
            if rem==0:
                digits[i]+=1
                return digits
            else:
                digits[i]=s%10
            i-=1
        return [1]+digits

            
            
        