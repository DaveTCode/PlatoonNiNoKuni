from hand import Hand

CARDS_IN_CAMPAIGN = 10
HANDS_IN_CAMPAIGN = 5

class Campaign():
    '''
        A campaign consists of a set of cards spread over a fixed number of 
        hands ordered however the player chooses.
    '''

    def __init__(self, cards):
        assert(len(cards) == CARDS_IN_CAMPAIGN)

        self.cards = cards
        self.hands = [Hand([]) for _ in range(HANDS_IN_CAMPAIGN)]

    def remaining_cards(self):
        '''
            List of the remaining cards which have not been allocated to any 
            hand.
        '''
        return [card for card in self.cards if not card in sum(map(lambda h: h.cards, self.hands), []) ]

    def add_card_to_hand(self, hand_index, card):
        '''
            Add a single card to a hand and return whether that card was valid 
            to be added.

            If it wasn't valid then the card will not be added.
        '''
        if card in self.cards and hand_index < HANDS_IN_CAMPAIGN and hand_index >= 0:
            return self.hands[hand_index].add_card(card)
        else:
            return False

    def remove_card_from_hand(self, hand_index, card):
        '''
            Remove a single card from a hand. If this leaves a hand in a bad 
            state then the remove will be reverted and this function will 
            return False.

            Otherwise returns True.
        '''
        if card in self.cards and hand_index < HANDS_IN_CAMPAIGN and hand_index >= 0:
            return self.hands[hand_index].remove_card(card)
        else:
            return False

    def clear_hands(self):
        '''
            Wipe all of the hands created so far.
        '''
        for hand in self.hands:
            hand.clear()

    def first_hand_w_card_type(self, card_type):
        '''
            Given a single card type this returns the first hand which contains
            that card.

            Returns None if can't find a hand.
        '''
        for hand in self.hands:
            for card in hand.cards:
                if card.name.lower() == card_type:
                    return self.hands.index(hand)

        return None

    def next_hand_w_no_card_type(self, *card_types):
        '''
            Given a set of card types we want to know which is the first hand 
            in the campaign that doesn't contain any of these types.

            Card types should be strings like "joker", "2" etc.
        '''
        for hand in self.hands:
            if len([card for card in hand.cards if card.name.lower() in card_types]) == 0:
                return self.hands.index(hand)

        return None

    def next_empty_hand(self):
        '''
            Find the next empty hand in the campaign.

            Returns an index.
        '''
        for hand in self.hands:
            if len(hand.cards) == 0:
                return self.hands.index(hand)

        return None

    def __str__(self):
        output = ""
        for hand in self.hands:
            output += str(hand)
            output += "-----------------------\n"

        return output