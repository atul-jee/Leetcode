class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        mx=0
        sc=0
        l=0
        r=len(tokens)-1
        while l<=r:
            if power>=tokens[l]:
                sc+=1
                power-=tokens[l]
                l+=1
                mx=max(sc,mx)
            elif sc>0:
                power+=tokens[r]
                sc-=1
                r-=1
            else:
                break
            
        return mx
        