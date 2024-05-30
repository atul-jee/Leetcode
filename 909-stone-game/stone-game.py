class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice,bob =0,0
        i,j = 0, len(piles) - 1
        turn = 1
        while  i<j:
            if turn :
                alice += max(piles[i],piles[j])
                if piles[i] >= piles[j] :
                    i += 1
                else:
                    j -= 1
            else:
                bob += max(piles[i],piles[j])
                if piles[i] >= piles[j] :
                    i += 1
                else:
                    j -= 1
        
        return alice>bob