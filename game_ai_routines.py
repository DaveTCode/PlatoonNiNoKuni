import random
from campaign import HANDS_IN_CAMPAIGN

class GameAIRoutine():

    def __init__(self):
        pass

    def game_ai_campaign_allocation(self, campaign):
        '''
            Replicate the game AI method of allocating out cards to hands.

            Done in three steps:
            1) Allocate out all bishops then kings, left to right
            2) Allocate out any number cards to ensure that each hand has at
               least one card and the rest at random ensuring that if a hand
               contains a number card then all cards to it's right also do.
            3) Allocate out jokers from left to right.
        '''
        self.allocate_specials(campaign)

        self.allocate_numbers(campaign)

        self.allocate_jokers(campaign)

    def allocate_specials(self, campaign):
        '''
            Allocate out the special cards that are in the campaign.

            This is deterministic and is done by allocating all bishops left to 
            right  followed by all kings in the same manner. The rule is that each
            hand can have at most one special card.
        '''
        for special_type in ["bishop", "king"]:
            for card in [card for card in campaign.cards if card.name.lower() == special_type]:
                campaign.add_card_to_hand(campaign.next_hand_w_no_card_type("bishop", "king"), card)

    def allocate_numbers(self, campaign):
        '''
            Allocate number cards (including Queen and Jack) out between the 
            hands.

            This is based on a pseudo random algorithm and is probably not
            quite what the computer does.

            Each hand must have one card, so out of the number cards, one card
            is allocated to each empty hand. After that the remaining cards are 
            spread between a random number of piles ensuring that any pile 
            containing a number must also be followed by piles containing 
            numbers.
        '''
        # Randomize the number cards
        number_cards = sorted([card for card in campaign.cards if not card.is_special()], key=lambda *args: random.random())

        # Allocate one card per empty pile
        first_empty_hand = campaign.next_empty_hand()
        for hand_index in range(first_empty_hand, HANDS_IN_CAMPAIGN):
            card = number_cards.pop()
            campaign.add_card_to_hand(hand_index, card)

        # For the remaining numbers (if any) we decide how many piles to 
        # distribute over (at random) and then allocate from right to left.
        piles_to_use = random.randint(1, min(len(number_cards), HANDS_IN_CAMPAIGN))
        first_pile_to_use = HANDS_IN_CAMPAIGN - piles_to_use
        for card in number_cards:
            hand_index = (number_cards.index(card) % piles_to_use) + first_pile_to_use
            campaign.add_card_to_hand(hand_index, card)

    def allocate_jokers(self, campaign):
        '''
            Allocate out all jokers that are in the campaign.

            This is deterministic although it is based on incomplete 
            information.
            Jokers are allocated left to right after all other cards have been 
            allocated.

            It's possible that this isn't what the computer does. More research 
            required @@@TODO.
        '''
        for card in [card for card in campaign.cards if card.name.lower() == "joker"]:
            campaign.add_card_to_hand(campaign.next_hand_w_no_card_type("joker"), card)