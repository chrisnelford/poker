import unittest

import sys
sys.path.insert(0, "C:\workspace\poker")
from poker_player import PokerPlayer


class TestStrategy(unittest.TestCase):

    def setUp(self):
        self.player = PokerPlayer(["Matt", "James", "Mark"])

    def test_starting_conditions(self):
        self.assertEqual(self.player.pots,
                         {"Chris":100, "Matt":100, "James":100, "Mark":100})

    def test_dealing_cards(self):

        # Deal the player a new hand.
        self.player.start_new_hand(["KC", "AS"])
        self.assertEqual(self.player.cards_in_hand, ["KC", "AS"])
        self.assertEqual(self.player.cards_on_table, [])

        # Show the flop.
        self.player.add_cards_on_table(["AC", "5H", "10D"])
        self.assertEqual(self.player.cards_in_hand, ["KC", "AS"])
        self.assertEqual(self.player.cards_on_table, ["AC", "5H", "10D"])

    def test_first_action(self):

        # Ask the player to take its turn.
        action = self.player.act()
        self.assertIn(action.action_type, ["Fold", "Bet"])

        if action.action_type == "Fold":
            self.assertEqual(action.amount, 0)

    
if __name__ == "__main__":
    unittest.main()
