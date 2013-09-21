import re
import argparse
from campaign_permutation_comparison import CampaignPermutationComparison
from campaign import Campaign
from card import Card
from game_ai_routines import GameAIRoutine

class Player():
    def __init__(self, is_random, is_ai):
        self.is_random = is_random
        self.is_ai = is_ai
        self.campaign = None

class Game():

    def __init__(self):
        self.player_1 = None
        self.player_2 = None

    def parse_command_line(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-p1r", 
                            "--player_1_random", 
                            help="Set if player one's cards are to be determined randomly.",
                            dest="is_player_1_random",
                            action="store_true")
        parser.add_argument("-p1nr",
                            "--player_1_user_picked",
                            help="Set if player one's cards are to be picked manually.",
                            dest="is_player_1_random",
                            action="store_false")
        parser.add_argument("-p2r", 
                            "--player_2_random", 
                            help="Set if player two's cards are to be determined randomly.",
                            dest="is_player_2_random",
                            action="store_true")
        parser.add_argument("-p2nr",
                            "--player_2_user_picked",
                            help="Set if player two's cards are to be picked manually.",
                            dest="is_player_2_random",
                            action="store_false")

        parser.add_argument("-p1ai", 
                            "--player_1_ai", 
                            help="Set if player one's cards should be allocated according to the AI routine.", 
                            dest="is_player_1_ai",
                            action="store_true")
        parser.add_argument("-p1nai", 
                            "--player_1_not_ai", 
                            help="Set if player one's cards should be distributeed between hands manually.", 
                            dest="is_player_1_ai",
                            action="store_false")
        parser.add_argument("-p2ai", 
                            "--player_2_ai", 
                            help="Set if player two's cards should be allocated according to the AI routine.", 
                            dest="is_player_2_ai",
                            action="store_true")
        parser.add_argument("-p2nai", 
                            "--player_2_not_ai", 
                            help="Set if player two's cards should be distributeed between hands manually.", 
                            dest="is_player_2_ai",
                            action="store_false") 
        result = parser.parse_args()

        self.player_1 = Player(result.is_player_1_random, result.is_player_1_ai)
        self.player_2 = Player(result.is_player_2_random, result.is_player_2_ai)
        
    def create_campaign(self, player):
        cards = []
        if player.is_random:
            cards = Card.get_random_set_of_cards(10)
        else:
            cards = [] # TODO - branch
        player.campaign = Campaign(cards)

        if player.is_ai:
            print "Auto distributing cards based on AI routine"
            GameAIRoutine().game_ai_campaign_allocation(player.campaign)
        else:
            print "Manually distributing cards for player"
            print "----"
            print "Enter the hand index [0,4] followed by a comma followed by the card to add in short form (4h, rj)"
            while len(cards) > 0:
                print "-------"
                print "Cards remaining: " + ",".join(map(lambda x: x.short_form(), cards))
                print "-------"
                entry = raw_input("Next entry: ")
                m = re.match("([0-4]),(\w{2})", entry)
                if re.match("[0-4],\w{2}", entry) != None:
                    hand_index = int(m.groups()[0])
                    card = Card.get_card_from_short_form(m.groups()[1])

                    if card != None and card in cards:
                        if player.campaign.add_card_to_hand(hand_index, card):
                            cards.remove(card)

    def run(self):
        self.parse_command_line()

        self.create_campaign(self.player_1)
        self.create_campaign(self.player_2)

        comparer = CampaignPermutationComparison()
        comparer.compare_campaigns(self.player_1.campaign, self.player_2.campaign)

        print "Player 1 campaign:"
        print self.player_1.campaign
        print "-----"
        print "Player 2 campaign:"
        print self.player_2.campaign
        print "-----"
        print comparer

if __name__ == '__main__':
    Game().run()