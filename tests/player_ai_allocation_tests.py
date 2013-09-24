import unittest
from Platoon.player_ai import PlayerAI
from Platoon.campaign import Campaign
from Platoon.card import Card

class PlayerAIAllocationTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.two_k_campaign = Campaign([Card.king_hearts, Card.king_spades, Card.two_hearts, Card.three_hearts, 
                                        Card.four_hearts, Card.five_hearts, Card.six_hearts, Card.seven_hearts, 
                                        Card.eight_hearts, Card.nine_hearts])
        self.k_bishop_campaign = Campaign([Card.bishop_hearts, Card.king_spades, Card.two_hearts, Card.three_hearts, 
                                           Card.four_hearts, Card.five_hearts, Card.six_hearts, Card.seven_hearts, 
                                           Card.eight_hearts, Card.nine_hearts])
        self.k_bishop_joker_campaign = Campaign([Card.king_hearts, Card.bishop_spades, Card.joker_red, Card.three_hearts, 
                                                 Card.four_hearts, Card.five_hearts, Card.six_hearts, Card.seven_hearts, 
                                                 Card.eight_hearts, Card.nine_hearts])
        self.no_special_campaign = Campaign([Card.nine_clubs, Card.three_spades, Card.two_hearts, Card.three_hearts, 
                                                      Card.four_hearts, Card.five_hearts, Card.six_hearts, Card.seven_hearts, 
                                                      Card.eight_hearts, Card.nine_hearts])

    def setUp(self):
        '''
            Clear all campaigns each time we run a test.
        '''
        for campaign in vars(self).values():
            if isinstance(campaign, Campaign):
                campaign.clear_hands()

    def testAllAllocation(self):
        for campaign in [campaign for var in vars(self).values() if isinstance(var, Campaign)]:
            PlayerAI().distribute_hands(campaign)
            for hand in campaign.hands:
                self.assertNotEqual(len(hand.cards), 0)

    def testHandValidity(self):
        for campaign in [campaign for var in vars(self).values() if isinstance(var, Campaign)]:
            PlayerAI().distribute_hands(campaign)
            for hand in campaign.hands:
                self.assertTrue(hand.is_valid())

    def testKingAllocation(self):
        for campaign in [campaign for var in vars(self).values() if isinstance(var, Campaign)]:
            PlayerAI().distribute_hands(campaign)

            for hand in campaign.hands():
                if hand.contains_card("king"):
                    self.assertEqual(len(hand.cards), 1)