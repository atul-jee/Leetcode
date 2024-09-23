from collections import defaultdict
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        d=defaultdict(int)
        for ele in message:
            d[ele]+=1
        count=0
        for ele in bannedWords:
            if d[ele]>0:
                count+=d[ele]
                d[ele]=0
                
            if count>=2:
                break
        return True if count>=2 else False

            
            



        