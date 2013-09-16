import random
from campaign import HANDS_IN_CAMPAIGN

EMPTY = 1
KING = 2
BISHOP = 4
JOKER = 8
NUMBERS = 16

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
    for bishop in [card for card in campaign.cards if card.name.lower() == "bishop"]:
        campaign.add_card_to_hand(next_no_special(), bishop)
        hand_state[next_no_special()] |= BISHOP

    for king in [card for card in campaign.cards if card.name.lower() == "king"]:
        campaign.add_card_to_hand(next_no_special(), king)
        hand_state[next_no_special()] |= KING

    # 2nd step
    # Allocate out any number cards at random between remaining hands
    # - Each hand must have one card so place one per empty hand first
    # - Of the remaining cards allocate out at random between all previously 
    #   empty piles.
    first_empty_hand = next_no_special()
    hands_to_distribute_over = HANDS_IN_CAMPAIGN - first_empty_hand
    number_cards = random.shuffle([card for card in campaign.cards if not card.is_special()])
    for hand_index in range(first_empty_hand, HANDS_IN_CAMPAIGN):
        campaign.add_card_to_hand(hand_index, number_cards[hand_index - first_empty_hand])
        hand_state[hand_index] |= NUMBERS

    

    # Last step
    # Add any jokers to piles. Order is left to right.
    # @@@TODO - Unsure whether this is what computer actually does...
    for joker in [card for card in campaign.cards if card.name.lower() == "joker"]:
        campaign.add_card_to_hand(next_no_joker(), joker)
        hand_state[next_no_joker()] |= JOKER
    