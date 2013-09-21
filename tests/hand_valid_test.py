import unittest
from Platoon.hand import Hand
from Platoon.card import Card

class HandValidatorTests(unittest.TestCase):

    def testEmptyHand(self):
        hand = Hand([])
        self.assertEqual(hand.is_valid(), True)

    def testJokerHand(self):
        hand = Hand([Card.joker_red])
        self.assertEqual(hand.is_valid(), False)

    def testJokerPlusHand(self):
        hand = Hand([Card.joker_red, Card.seven_diamonds])
        self.assertEqual(hand.is_valid(), True)

    def testTwoJokerHand(self):
        hand = Hand([Card.joker_red, Card.joker_red])
        self.assertEqual(hand.is_valid(), False)

    def testKingHand(self):
        hand = Hand([Card.king_spades])
        self.assertEqual(hand.is_valid(), True)

    def testKingJokerHand(self):
        hand = Hand([Card.king_spades, Card.joker_red])
        self.assertEqual(hand.is_valid(), True)

    def testTwoKingHand(self):
        hand = Hand([Card.king_spades, Card.king_hearts])
        self.assertEqual(hand.is_valid(), False)

    def testKingBishopHand(self):
        hand = Hand([Card.king_spades, Card.bishop_hearts])
        self.assertEqual(hand.is_valid(), False)

    def testBishopHand(self):
        hand = Hand([Card.bishop_spades])
        self.assertEqual(hand.is_valid(), True)

    def testBishopJokerHand(self):
        hand = Hand([Card.bishop_spades, Card.joker_red])
        self.assertEqual(hand.is_valid(), True)

    def testTwoBishopHand(self):
        hand = Hand([Card.bishop_spades, Card.bishop_diamonds])
        self.assertEqual(hand.is_valid(), False)

    def testNumberHand(self):
        hand = Hand([Card.two_hearts])
        self.assertEqual(hand.is_valid(), True)

    def testDuplicate(self):
        hand = Hand([Card.two_hearts, Card.two_hearts])
        self.assertEqual(hand.is_valid(), False)

def main():
    unittest.main()

if __name__ == '__main__':
    main()