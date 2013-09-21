import unittest
from Platoon.card import Card

class CardIsSpecialTests(unittest.TestCase):

    def testIsSpecialJoker(self):
        self.assertEqual(Card.joker_red.is_special(), True)

    def testIsSpecialKing(self):
        self.assertEqual(Card.king_hearts.is_special(), True)

    def testIsSpecialBishop(self):
        self.assertEqual(Card.bishop_spades.is_special(), True)

    def testIsSpecialNumber(self):
        self.assertEqual(Card.three_diamonds.is_special(), False)

    def testIsSpecialQueen(self):
        self.assertEqual(Card.queen_clubs.is_special(), False)

    def testIsSpecialJack(self):
        self.assertEqual(Card.jack_hearts.is_special(), False)        

class CardNameTests(unittest.TestCase):
    def testTwoHearts(self):
        self.assertEqual(str(Card.two_hearts), "2 of hearts")

    def testKingSpades(self):
        self.assertEqual(str(Card.king_spades), "king of spades")

    def testJoker(self):
        self.assertEqual(str(Card.joker_red), "joker")

class CardCollectionTests(unittest.TestCase):
    def testRightNumCards(self):
        self.assertEqual(len(Card.get_random_set_of_cards(2)), 2)

class ShortFormTests(unittest.TestCase):

    def testShortFormNumber(self):
        self.assertEqual(Card.two_hearts.short_form(), "2h")

    def testShortFormTen(self):
        self.assertEqual(Card.ten_clubs.short_form(), "tc")

    def testGetByShortForm(self):
        self.assertEqual(Card.get_card_from_short_form("tc"), Card.ten_clubs)
        self.assertEqual(Card.get_card_from_short_form("js"), Card.jack_spades)

def main():
    unittest.main()

if __name__ == '__main__':
    main()