class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        
        res = deque()
        while deck:
            if res:
                res.appendleft(res.pop()) #this is the reverse of moving a card from top of deck to bottom of deck
            res.appendleft(deck.pop()) #this is the reverse of playing the card from the top of the deck
        
        return res