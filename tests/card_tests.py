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

def main():
    unittest.main()

if __name__ == '__main__':
    main()