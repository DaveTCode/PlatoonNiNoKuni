class GameAI():
    '''
        Override to implement an AI player for this game.

        Must implement two functions:
        - distribute_hands to allocate the cards of a campaign to the hands
        - play_hand to select from an unused hand in each campaign to compete
          against each other.
    '''

    def __init__(self, description):
        self.description = description

    def distribute_hands(self, campaign):
        '''
            Result of this function should be that the campaign has all cards
            allocated into the separate hands.
        '''
        raise NotImplementedError("Must override this method")

    def play_hand(self, campaign, opponent_campaign):
        '''
            Given a campaign with any number of hands remaining to play, this
            routine must be overriden to select from one of the remaining pairs 
            of hands.
        '''
        raise NotImplementedError("Must overide this method")