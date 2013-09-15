from campaign import HANDS_IN_CAMPAIGN

EMPTY = 1
KING = 2
BISHOP = 4
JOKER = 8

def game_ai_campaign_allocation(campaign):
    '''
        Replicate the game AI method of allocating out cards to hands.
    '''
    hand_state = [EMPTY for _ in range(HANDS_IN_CAMPAIGN)]

    def next_no_special():
        '''
            The next space in the hand set which doesn't contain a special
        '''
        index = 0
        for hand in hand_state:
            if (hand & KING) or (hand & BISHOP):
                return index

            index += 1

        return index

    def next_no_joker():
        '''
         Find the next hand that doesn't have a joker in
        '''
        index = 0
        for hand in hand_state:
            if hand & JOKER:
                return index

            index += 1

        return index

    # 1st step
    # Allocate out special cards left to right. Non-random. Bishops first.
    for bishop in [card for card in campaign.cards if card.name == "bishop"]:
        campaign.add_card_to_hand(next_no_special(), bishop)
        hand_state[next_no_special()] = 1

    for king in [card for card in campaign.cards if card.name == "king"]:
        campaign.add_card_to_hand(next_no_special(), king)

    # 2nd step
    # Allocate out any number cards at random between remaining hands
    first_empty_hand = next_no_special()
    hands_to_distribute_over = HANDS_IN_CAMPAIGN - first_empty_hand
    for hand_index in range(first_empty_hand, HANDS_IN_CAMPAIGN):

    # Last step
    # Add any jokers to piles. Order is left to right.
    