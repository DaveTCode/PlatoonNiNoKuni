import unittest
from hand import Hand
from card import Card

class CardNameTests(unittest.TestCase):
    def testTwoHearts(self):
        self.assertEqual(str(Card.two_hearts), "2 of hearts")

    def testKingSpades(self):
        self.assertEqual(str(Card.king_spades), "king of spades")

    def testJoker(self):
        self.assertEqual(str(Card.joker_red), "joker")

class HandValueTests(unittest.TestCase):

    def testOneCard(self):
        hand_1 = Hand([Card.two_hearts])
        self.assertEqual(hand_1.total(), 2)

    def testTwoCards(self):
        hand_1 = Hand([Card.two_hearts, Card.nine_clubs])
        self.assertEqual(hand_1.total(), 11)

    def testMultipleCards(self):
        hand_1 = Hand([Card.two_hearts, Card.nine_clubs, Card.seven_diamonds, Card.three_clubs, Card.jack_hearts, Card.queen_spades])
        self.assertEqual(hand_1.total(), 41)

class HandCompareTests(unittest.TestCase):

    def testEqualNumberHand(self):
        hand_1 = Hand([Card.two_hearts])
        hand_2 = Hand([Card.two_clubs])
        self.assertEqual(hand_1.compare(hand_2), hand_2.compare(hand_1))

    def testUnequalHands1(self):
        hand_1 = Hand([Card.two_hearts])
        hand_2 = Hand([Card.two_clubs, Card.three_hearts])
        self.assertEqual(hand_1.compare(hand_2), -1)

    def testUnequalHands2(self):
        hand_1 = Hand([Card.two_hearts, Card.jack_spades])
        hand_2 = Hand([Card.two_clubs, Card.three_hearts])
        self.assertEqual(hand_1.compare(hand_2), 1)

    def testEqualHandsWithSwap(self):
        hand_1 = Hand([Card.two_hearts, Card.joker_red])
        hand_2 = Hand([Card.two_clubs])
        self.assertEqual(hand_1.compare(hand_2), hand_2.compare(hand_1))

    def testUnequalHandsWithSwap(self):
        hand_1 = Hand([Card.three_hearts, Card.joker_red])
        hand_2 = Hand([Card.two_clubs])
        self.assertEqual(hand_1.compare(hand_2), -1)
        self.assertEqual(hand_2.compare(hand_1), 1)

    def testKingAgainstCards(self):
        hand_1 = Hand([Card.king_hearts])
        hand_2 = Hand([Card.two_hearts, Card.nine_clubs, Card.seven_diamonds, Card.three_clubs, Card.jack_hearts, Card.queen_spades])

        self.assertEqual(hand_1.compare(hand_2), 1)
        self.assertEqual(hand_2.compare(hand_1), -1)

    def testKingAgainstKing(self):
        hand_1 = Hand([Card.king_hearts])
        hand_2 = Hand([Card.king_spades])

        self.assertEqual(hand_1.compare(hand_2), hand_2.compare(hand_1))

    def testKingAgainstKingPlus(self):
        hand_1 = Hand([Card.king_hearts, Card.two_hearts])
        hand_2 = Hand([Card.king_spades])

        self.assertEqual(hand_1.compare(hand_2), 1)
        self.assertEqual(hand_2.compare(hand_1), -1)

    def testKingAgainstBishop(self):
        hand_1 = Hand([Card.king_hearts, Card.two_hearts])
        hand_2 = Hand([Card.bishop_hearts])

        self.assertEqual(hand_1.compare(hand_2), -1)
        self.assertEqual(hand_2.compare(hand_1), 1)

    def testBothBishop(self):
        hand_1 = Hand([Card.bishop_spades])
        hand_2 = Hand([Card.bishop_hearts])

        self.assertEqual(hand_1.compare(hand_2), hand_2.compare(hand_1))

    def testOneBishopNoKing(self):
        hand_1 = Hand([Card.bishop_spades, Card.seven_diamonds])
        hand_2 = Hand([Card.two_hearts])

        self.assertEqual(hand_1.compare(hand_2), -1)
        self.assertEqual(hand_2.compare(hand_1), 1)

def main():
    unittest.main()

if __name__ == '__main__':
    main()