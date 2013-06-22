class Action:
    action_types = ["Fold", "Bet"]
    
    def __init__(self, player, action_type, amount=0):

        if action_type not in Action.action_types:
            raise Exception("Invalid Action. Action type: {}, Amount: {}.".format(action_type, amount))
        
        self.player = player
        self.action_type = action_type
        self.amount = amount
        

# The strategy class decides what to do at each stage of the game.
#
# @param players: A list of the players at the table starting with the player
# to the left.
#
class PokerPlayer:
    def __init__(self, players):
        self.cards_in_hand = []
        self.cards_on_table = []
        self.players = players
        self.name = "Chris"

        # Set up initial pots.
        self.pots = {player: 100 for player in players}
        self.pots[self.name] = 100

    def start_new_hand(self, hand):
        self.cards_in_hand = hand
        self.cards_on_table = []

    def add_cards_on_table(self, cards):
        self.cards_on_table.extend(cards)

    def act(self):
        return Action(self.name, "Fold")
