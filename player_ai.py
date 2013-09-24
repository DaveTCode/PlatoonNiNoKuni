from ai import GameAI

class PlayerAI(GameAI):

    def __init__(self):
        self.winning_hands = 0
        self.losing_hands = 0
        self.backup_hands = 0
        GameAI.__init__(self, "AI which acts how a player would/should assuming playing against the house")

    def distribute_hands(self, campaign):
        # Kings and bishops first. They go on their own to start with.
        self._allocate_specials(campaign)

        # Add joker to bishop for all bishop+joker pairs.
        self._allocate_joker_bishop_pairs(campaign)

        # Allocate out the number cards
        number_cards = [card for card in campaign.remaining_cards() if not card.is_special()]
        number_cards.sort(key=lambda card: card.value)
        
        # If there are any jokers left then we want a pile with one joker plus 
        # the lowest card remaining for each joker.
        for joker in [card for card in campaign.remaining_cards() if card.name.lower() == "joker"]:
            hand_ix = campaign.next_empty_hand()
            campaign.add_card_to_hand(hand_ix, number_cards.pop(0))
            campaign.add_card_to_hand(hand_ix, joker)
            winning_hands += 1 # Low number + joker => winning hand

        # Allocate the number cards
        current_hand = campaign.next_empty_hand()
        while number_cards:
            current_hand_value = campaign.hands[current_hand].total()

            if current_hand_value > 20:
                current_hand = campaign.next_empty_hand()

                if not current_hand:
                    # We've reached the end of the hands with cards still to 
                    # use up.
                    current_hand = campaign.hands

                card = number_cards.pop()
            else:
                remaining_empty_hands = len([hand for hand in campaign.hands if not hand.cards])
                if remaining_empty_hands >= len(number_cards):
                    current_hand = campaign.next_empty_hand()
                    card = self._best_card_to_add(campaign.hands[current_hand], number_cards)
                    number_cards.remove(card)
                else:
                    # In this case we are adding a card to a hand with some 
                    # numbers already.
                    # We want to get as close to 20 as possible with priority
                    # going to just 21 over 19, 22 over 18 etc.
                    card = number_cards

            campaign.add_card_to_hand(current_hand, card)

    def _allocate_specials(self, campaign):
        for card in [card for card in campaign.cards if card.name.lower() in ["king", "bishop"]]:
            campaign.add_card_to_hand(campaign.next_empty_hand(), card)

            if card.name.lower() == "king":
                self.winning_hands += 1
            elif card.name.lower() == "bishop":
                self.losing_hands += 1

    def _allocate_joker_bishop_pairs(self, campaign):
        for joker in [card for card in campaign.remaining_cards() if card.name.lower() == "joker"]:
            bishop_hand_ix = campaign.first_hand_w_card_type("bishop", "joker")
            if bishop_hand_ix != None:
                campaign.add_card_to_hand(bishop_hand_ix, joker)
                self.winning_hands += 1 # Bishop + joker => winning hand
                self.losing_hands -= 1 # Was previously a losing hand (bishop only)

    def _best_card_to_add(self, hand, number_cards):
        '''
            If we have a hand with some number cards in it and want to add
            a card, then we want to get as close to 20 as possible in one step.

            This function does that and puts precedence on the higher in a tie.
        '''
        total = hand.total()
        current_best_card = None

        for card in number_cards:
            if (not current_best_card or 
                20 - (total + card.value) < 20 - (total + current_best_card.value)):
                current_best_card = card
            elif 20 - (total + card.value) == 20 - (total + current_best_card.value):
                if total + card.value > total + current_best_card.value:
                    current_best_card = card

        return current_best_card