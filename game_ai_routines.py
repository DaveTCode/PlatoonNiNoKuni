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

    allocate_specials(hand_states, campaign)

    allocate_numbers(hand_states, campaign)

    allocate_jokers(hand_states, campaign)
    
def next_no_special(hand_states):
    '''
        The next space in the hand set which doesn't contain a special
    '''
    index = 0
    for hand in hand_states:
        if (hand & KING) or (hand & BISHOP):
            return index

        index += 1

    return index

def next_no_joker(hand_states):
    '''
        Find the next hand that doesn't have a joker in
    '''
    index = 0
    for hand in hand_states:
        if hand & JOKER:
            return index

        index += 1

    return index

def allocate_specials(hand_states, campaign):
    '''
        Allocate out the special cards that are in the campaign.

        This is deterministic and is done by allocating all bishops left to 
        right  followed by all kings in the same manner. The rule is that each
        hand can have at most one special card.
    '''
    for special_type in [("bishop", BISHOP), ("king", KING)]:
        for card in [card for card in campaign.cards if card.name.lower() == special_type[0]]:
            campaign.add_card_to_hand(next_no_special(hand_states), card)
            hand_states[next_no_special(hand_states)] |= special_type[1]

def allocate_numbers(hand_states, campaign):
    '''
        Allocate number cards (including Queen and Jack) out between the hands.

        This is based on a pseudo random algorithm and is probably not quite 
        what the computer does.

        Each hand must have one card, so out of the number cards, one card is 
        allocated to each empty hand. After that, the remaining cards are split 
        between any number piles and a random number of the piles containing
        kings.

        The kings are filled right to left as any pile to the right of a pile 
        containing numbers must also contain numbers.
    '''
    # Randomize the number cards
    number_cards = random.shuffle([card for card in campaign.cards if not card.is_special()])

    # Allocate one card per empty pile
    first_empty_hand = next_no_special(hand_states)
    for hand_index in range(first_empty_hand, HANDS_IN_CAMPAIGN):
        card = number_cards.pop()
        campaign.add_card_to_hand(hand_index, card)
        hand_states[hand_index] |= NUMBERS

    # Decide how many king cards to put numbers on.
    num_kings = len([card for card in campaign.cards if card.name.lower() == "king"])


def allocate_jokers(hand_states, campaign):
    '''
        Allocate out all jokers that are in the campaign.

        This is deterministic although it is based on incomplete information. 
        Jokers are allocated left to right after all other cards have been 
        allocated.

        It's possible that this isn't what the computer does. More research 
        required TODO.
    '''
    for card in [card for card in campaign.cards if card.name.lower() == "joker"]:
        campaign.add_card_to_hand(next_no_joker(hand_states), card)
        hand_states[next_no_joker(hand_states)] |= JOKER