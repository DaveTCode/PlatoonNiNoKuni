import unittest
from hand import Hand
from card import Card
from campaign import Campaign

class CampaignTests(unittest.TestCase):

    def setUp(self):
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

def main():
    unittest.main()

if __name__ == '__main__':
    main()