import unittest
from Platoon.ai import GameAI

class AIMissingImpl(GameAI):
    def __init__(self):
        GameAI.__init__(self, "AI missing implementation")

class AIBaseTests(unittest.TestCase):

    def testMissingDistributeFunction(self):
        with self.assertRaises(NotImplementedError):
            AIMissingImpl().distribute_hands(None)

    def testMissingPlayHandFunction(self):
        with self.assertRaises(NotImplementedError):
            AIMissingImpl().play_hand(None, None)

def main():
    unittest.main()

if __name__ == '__main__':
    main()