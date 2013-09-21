import unittest
from Platoon.card import Card
from Platoon.campaign import Campaign
from Platoon.game_ai_routines import GameAIRoutine

class AIAllocationTests(unittest.TestCase):

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

    def testSpecialLocationTwoK(self):
        GameAIRoutine().game_ai_campaign_allocation(self.two_k_campaign)
        self.assertEqual(self.two_k_campaign.hands[0].cards[0].name.lower(), "king")
        self.assertEqual(self.two_k_campaign.hands[1].cards[0].name.lower(), "king")

    def testSpecialLocationKB(self):
        GameAIRoutine().game_ai_campaign_allocation(self.k_bishop_campaign)
        self.assertEqual(self.k_bishop_campaign.hands[0].cards[0].name.lower(), "bishop")
        self.assertEqual(self.k_bishop_campaign.hands[1].cards[0].name.lower(), "king")

    def testSpecialLocationKBJ(self):
        GameAIRoutine().game_ai_campaign_allocation(self.k_bishop_joker_campaign)
        self.assertEqual(self.k_bishop_joker_campaign.hands[0].cards[0].name.lower(), "bishop")
        self.assertEqual(self.k_bishop_joker_campaign.hands[1].cards[0].name.lower(), "king")
        self.assertEqual(self.k_bishop_joker_campaign.hands[0].cards[-1].name.lower(), "joker")

def main():
    unittest.main()

if __name__ == '__main__':
    main()