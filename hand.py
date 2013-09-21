import operator

class Hand():
    '''
        Represents a hand instance in platoon
    '''

    def __init__(self, cards):
        self.cards = cards

    def cards_by_face_value(self):
        '''
            Return a list of the cards ordered by face value
        '''
        return sorted(self.cards, key=lambda card: card.value)

    def contains_card(self, name):
        '''
            Check whether this hand contains a card of a specific type
        '''
        return self.count_card(name) > 0

    def count_card(self, name):
        '''
            Determine how many of a particular card type there are.
        '''
        count = 0
        for card in self.cards:
            if card.name.lower() == name.lower():
                count += 1

        return count

    def total(self):
        '''
            Total face value of the cards.
        '''
        return reduce(lambda x, y: x + y, [card.value for card in self.cards])

    def clear(self):
        '''
            Remove any cards in the hand.
        '''
        del self.cards[:]

    def compare(self, other):
        '''
            Compare two hands:
            1 if this hand wins
            0 if draw
            -1 if this hand loses
        '''
        # Swap the hands if either but no both hands contain a joker
        swapped = operator.xor(self.contains_card("joker"), other.contains_card("joker"))

        # Handle the case where our hand has a king
        if self.contains_card("king"):
            if other.contains_card("bishop"):
                return 1 if swapped else -1
            elif other.contains_card("king"):
                pass # Allow to fall through to a count of cards
            else:
                return -1 if swapped else 1

        # Handle the case where the other hand has a king
        if other.contains_card("king"):
            if self.contains_card("bishop"):
                return -1 if swapped else 1
            elif self.contains_card("king"):
                pass # Allow to fall through to a count of cards
            else:
                return 1 if swapped else -1

        # Handle the case where there is a bishop but no king (king case covered above)
        if self.contains_card("bishop") and other.contains_card("bishop"):
            return 0
        elif self.contains_card("bishop"):
            return 1 if swapped else -1
        elif other.contains_card("bishop"):
            return -1 if swapped else 1

        # Handles the case where either there were kings on each side
        # or the fall through case where we need to compare values.
        if self.total() == other.total():
            return 0
        elif self.total() < other.total():
            return 1 if swapped else -1
        else:
            return -1 if swapped else 1
        
    def add_card(self, card):
        '''
            This function is also responsible for verifying that the card is
            allowed to be added to the hand. There are various rules that 
            apply:
            - A joker must not be the only card in a hand
            - Each hand may only contain one of each special card
            - A hand may not contain a bishop and a king
            - A hand must contain at least one card (this function guarantees
                that automatically)
        '''
        self.cards.append(card)
        if not self.is_valid():
            self.cards.pop()
            return False

        return True

    def remove_card(self, card):
        '''
            Remove a specific instance of a card.

            Note that since cards are actually static objects, if there were 
            two identical cards in a hand this would remove both.

            There shouldn't be anyway.
        '''
        if card in self.cards:
            ix = self.cards.index(card)
            self.cards.remove(card)

            if not self.is_valid():
                self.cards.insert(ix, card)
                return False

            return True

        return False

    def is_valid(self):
        '''
            Determine whether the hand contains a valid collection of cards.

            Note that this does not test emptiness.
        '''
        if len(self.cards) == 1 and self.contains_card("joker"):
            return False
        elif (self.count_card("joker") > 1 or
              self.count_card("bishop") > 1 or
              self.count_card("king") > 1):
            return False
        elif self.count_card("bishop") == 1 and self.count_card("king") == 1:
            return False
        elif len(set(self.cards)) != len(self.cards):
            return False
        else: 
            return True

    def __str__(self):
        name = ""
        for card in self.cards_by_face_value():
            name += str(card) + "\n"

        return name
