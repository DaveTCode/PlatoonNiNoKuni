class Card():
    '''
        Represents a single card type
    '''

    def __init__(self, value, name, suit):
        self.value = value
        self.name = name
        self.suit = suit

    def __str__(self):
        if self.name.lower() == "joker":
            return self.name.lower()
        else:
            return self.name.lower() + " of " + self.suit.lower()

Card.two_hearts = Card(2, "2", "hearts")
Card.three_hearts = Card(3, "3", "hearts")
Card.four_hearts = Card(4, "4", "hearts")
Card.five_hearts = Card(5, "5", "hearts")
Card.six_hearts = Card(6, "6", "hearts")
Card.seven_hearts = Card(7, "7", "hearts")
Card.eight_hearts = Card(8, "8", "hearts")
Card.nine_hearts = Card(9, "9", "hearts")
Card.ten_hearts = Card(10, "10", "hearts")
Card.jack_hearts = Card(10, "Jack", "hearts")
Card.queen_hearts = Card(10, "Queen", "hearts")
Card.king_hearts = Card(11, "King", "hearts")
Card.bishop_hearts = Card(1, "Bishop", "hearts")

Card.two_spades = Card(2, "2", "spades")
Card.three_spades = Card(3, "3", "spades")
Card.four_spades = Card(4, "4", "spades")
Card.five_spades = Card(5, "5", "spades")
Card.six_spades = Card(6, "6", "spades")
Card.seven_spades = Card(7, "7", "spades")
Card.eight_spades = Card(8, "8", "spades")
Card.nine_spades = Card(9, "9", "spades")
Card.ten_spades = Card(10, "10", "spades")
Card.jack_spades = Card(10, "Jack", "spades")
Card.queen_spades = Card(10, "Queen", "spades")
Card.king_spades = Card(11, "King", "spades")
Card.bishop_spades = Card(1, "Bishop", "spades")

Card.two_clubs = Card(2, "2", "clubs")
Card.three_clubs = Card(3, "3", "clubs")
Card.four_clubs = Card(4, "4", "clubs")
Card.five_clubs = Card(5, "5", "clubs")
Card.six_clubs = Card(6, "6", "clubs")
Card.seven_clubs = Card(7, "7", "clubs")
Card.eight_clubs = Card(8, "8", "clubs")
Card.nine_clubs = Card(9, "9", "clubs")
Card.ten_clubs = Card(10, "10", "clubs")
Card.jack_clubs = Card(10, "Jack", "clubs")
Card.queen_clubs = Card(10, "Queen", "clubs")
Card.king_clubs = Card(11, "King", "clubs")
Card.bishop_clubs = Card(1, "Bishop", "clubs")

Card.two_diamonds = Card(2, "2", "diamonds")
Card.three_diamonds = Card(3, "3", "diamonds")
Card.four_diamonds = Card(4, "4", "diamonds")
Card.five_diamonds = Card(5, "5", "diamonds")
Card.six_diamonds = Card(6, "6", "diamonds")
Card.seven_diamonds = Card(7, "7", "diamonds")
Card.eight_diamonds = Card(8, "8", "diamonds")
Card.nine_diamonds = Card(9, "9", "diamonds")
Card.ten_diamonds = Card(10, "10", "diamonds")
Card.jack_diamonds = Card(10, "Jack", "diamonds")
Card.queen_diamonds = Card(10, "Queen", "diamonds")
Card.king_diamonds = Card(12, "King", "diamonds")
Card.bishop_diamonds = Card(1, "Bishop", "diamonds")

Card.joker_red = Card(0, "Joker", None)
Card.joker_black = Card(0, "Joker", None)