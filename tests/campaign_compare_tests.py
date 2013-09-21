import unittest
from Platoon.campaign import Campaign
from Platoon.card import Card
from Platoon.campaign_permutation_comparison import CampaignPermutationComparison

class CampaignCompareTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def setUp(self):
        pass

    def testCompareAllWins(self):
        campaign1 = Campaign([Card.king_hearts, Card.king_spades, Card.king_clubs, Card.king_diamonds,
                              Card.jack_hearts, Card.queen_hearts, Card.ten_hearts, Card.nine_hearts,
                              Card.two_hearts, Card.three_hearts])
        campaign2 = Campaign([Card.four_hearts, Card.five_hearts, Card.six_hearts, Card.seven_hearts,
                              Card.four_clubs, Card.five_clubs, Card.six_clubs, Card.seven_clubs,
                              Card.four_spades, Card.five_spades])
        campaign1.add_card_to_hand(0, Card.king_hearts)
        campaign1.add_card_to_hand(1, Card.king_spades)
        campaign1.add_card_to_hand(2, Card.king_clubs)
        campaign1.add_card_to_hand(3, Card.king_diamonds)
        for ii in range(4, 10):
            campaign1.add_card_to_hand(4, campaign1.cards[ii])

        for ii in range(10):
            campaign2.add_card_to_hand(ii % 5, campaign2.cards[ii])

        comp = CampaignPermutationComparison()
        self.assertEqual(str(comp), "Comparison not done")
        comp.compare_campaigns(campaign1, campaign2)
        self.assertEqual(str(comp), "Wins  : 600\nLosses: 0\nDraws : 0")
        self.assertEqual(comp.score(), 600)
        self.assertEqual(comp.win, 600)
        self.assertEqual(comp.draw, 0)
        self.assertEqual(comp.loss, 0)