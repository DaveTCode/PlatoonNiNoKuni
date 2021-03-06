import unittest
from Platoon.hand import Hand
from Platoon.card import Card
from Platoon.campaign import Campaign

class CampaignTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.campaign = Campaign([Card.two_hearts, Card.three_hearts, Card.four_hearts, 
                                  Card.five_hearts, Card.six_hearts, Card.seven_hearts, 
                                  Card.eight_hearts, Card.king_hearts, Card.bishop_hearts, 
                                  Card.joker_red])

    def testCreateCampaignWrongNumCards(self):
        with self.assertRaises(AssertionError):
            campaign = Campaign([])

    def testAddRemoveCards(self):
        self.assertEqual(self.campaign.add_card_to_hand(0, Card.two_hearts), True)
        self.assertEqual(self.campaign.remove_card_from_hand(0, Card.two_hearts), True)
        self.campaign.clear_hands()

    def testAddBadCard(self):
        self.assertEqual(self.campaign.add_card_to_hand(0, Card.two_clubs), False)
        self.campaign.clear_hands()

    def testRemoveCardNotInCampaign(self):
        self.assertEqual(self.campaign.remove_card_from_hand(0, Card.two_clubs), False)
        self.campaign.clear_hands()

    def testRemoveCardNotInHand(self):
        self.assertEqual(self.campaign.remove_card_from_hand(0, Card.two_hearts), False)
        self.campaign.clear_hands()

    def testRemainingCards(self):
        self.campaign.clear_hands()
        self.assertEqual(Card.two_hearts in self.campaign.remaining_cards(), True)
        self.campaign.add_card_to_hand(0, Card.two_hearts)
        self.assertEqual(len(self.campaign.remaining_cards()), 9)
        self.campaign.add_card_to_hand(0, Card.six_hearts)
        self.assertEqual(len(self.campaign.remaining_cards()), 8)
        self.assertEqual(Card.two_hearts in self.campaign.remaining_cards(), False)

class CampaignFindHandTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.campaign = Campaign([Card.two_hearts, Card.three_hearts, Card.four_hearts, 
                                  Card.five_hearts, Card.six_hearts, Card.seven_hearts, 
                                  Card.eight_hearts, Card.king_hearts, Card.bishop_hearts, 
                                  Card.joker_red])
        self.campaign.add_card_to_hand(0, Card.bishop_hearts)
        self.campaign.add_card_to_hand(1, Card.two_hearts)
        self.campaign.add_card_to_hand(1, Card.joker_red)
        self.campaign.add_card_to_hand(2, Card.six_hearts)
        self.campaign.add_card_to_hand(3, Card.eight_hearts)

    def testFirstEmptyHand(self):
        self.assertEqual(self.campaign.next_empty_hand(), 4)

    def testNoEmptyHand(self):
        self.campaign.add_card_to_hand(4, Card.king_hearts)
        self.assertEqual(self.campaign.next_empty_hand(), None)
        self.campaign.remove_card_from_hand(4, Card.king_hearts)

    def testFirstHandMissingJoker(self):
        self.assertEqual(self.campaign.next_hand_w_no_card_type("joker"), 0)

    def testFirstHandMissingBishop(self):
        self.assertEqual(self.campaign.next_hand_w_no_card_type("bishop"), 1)

    def testFirstHandMissingEitherOfTwo(self):
        self.assertEqual(self.campaign.next_hand_w_no_card_type("bishop", "joker"), 2)

    def testFirstHandWBishop(self):
        self.assertEqual(self.campaign.first_hand_w_card_type("bishop"), 0)

    def testFirstHandWJoker(self):
        self.assertEqual(self.campaign.first_hand_w_card_type("joker"), 1)

    def testFirstHandNonExistent(self):
        self.assertEqual(self.campaign.first_hand_w_card_type("five"), None)

def main():
    unittest.main()

if __name__ == '__main__':
    main()