from hand import Hand

HANDS_IN_CAMPAIGN = 5

class Campaign():
    '''
        A campaign consists of 10 cards spread over 5 hands ordered however 
        the player chooses.
    '''

    def __init__(self, cards):
        self.cards = cards
        self.hands = [Hand() for _ in range(HANDS_IN_CAMPAIGN)]

    def add_card_to_hand(self, card, hand_index):
        '''
            Add a single card to a hand and return whether that card was valid 
            to be added.
        '''
        return self.hands[hand_index].add_card(card)

    def clear_hands(self):
        '''
            Wipe all of the hands created so far.
        '''
        self.hands = [Hand() for _ in range(HANDS_IN_CAMPAIGN)]