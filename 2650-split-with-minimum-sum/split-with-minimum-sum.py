class Solution:
    def splitNum(self, num: int) -> int:
        num=str(num)
        num=list(num)
        num.sort()
        f=''
        s=''
        for i in range(len(num)):
            if i%2==1:
                f+=num[i]
            else:
                s+=num[i]
        f=int(f)
        s=int(s)
        return f+s

        return num