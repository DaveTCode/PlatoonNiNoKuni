from campaign import HANDS_IN_CAMPAIGN
import itertools

class CampaignPermutationComparison():

    def __init__(self):
        self.win = 0
        self.draw = 0
        self.loss = 0

    def score(self):
        '''
            Total win loss record as single number. Win = 1, Loss = -1
        '''
        return self.win - self.loss

    def compare_campaigns(self, campaign1, campaign2):
        '''
            To compare two campaigns we take all permutations of both sets of
            hands and compare them adding the result.

            The result of this is @@@TODO
        '''
        assert(len(campaign1.hands) == len(campaign2.hands) and len(campaign1.hands) == HANDS_IN_CAMPAIGN)

        for permutation in [zip(x, range(HANDS_IN_CAMPAIGN)) for x in itertools.permutations(range(HANDS_IN_CAMPAIGN), HANDS_IN_CAMPAIGN)]:
            for pairing in permutation:
                s = campaign1.hands[pairing[0]].compare(campaign2.hands[pairing[1]])
                if s == 0:
                    self.draw += 1
                elif s == 1:
                    self.win += 1
                else:
                    self.loss += 1

        return self.score()

    def __str__(self):
        if self.win == 0 and self.draw == 0 and self.loss == 0:
            return "Comparison not done"
        else:
            return "Wins  : %d\nLosses: %d\nDraws : %d" % (self.win, self.loss, self.draw)