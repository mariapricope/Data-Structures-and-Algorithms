import unittest
from card_game_v3 import Card, Deck, Player, Game

class TestCard(unittest.TestCase):
    def test_card_initialisation(self):
        card = Card('Hearts', 'King')
        self.assertEqual(card.suit, 'Hearts')
        self.assertEqual(card.value, 'King')

    def test_get_value(self):
        card = Card('Diamonds', 'Ace')
        self.assertEqual(card.get_value(), 14)  # Ace should return 14

class TestDeck(unittest.TestCase):
    def test_deck_initialisation(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)  # Should have 52 cards initially

    def test_shuffle(self):
        deck = Deck()
        original_order = deck.cards.copy()
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_order)  # The deck should be shuffled

    def test_deal(self):
        deck = Deck()
        top_card = deck.deal()
        self.assertEqual(len(deck.cards), 51)  # Should have one less card after dealing
        self.assertIsInstance(top_card, Card)  # The dealt card should be an instance of Card

class TestPlayer(unittest.TestCase):
    def test_player_initialisation(self):
        player = Player(1, 100)
        self.assertEqual(player.id, 1)
        self.assertEqual(player.funds, 100)

    def test_bet(self):
        player = Player(1, 100)
        bet_amount = player.bet()
        self.assertEqual(bet_amount, 1)  # Bet should be 1
        self.assertEqual(player.funds, 99)  # Funds should decrease by 1

    def test_bet_no_funds(self):
        player = Player(1, 0)
        with self.assertRaises(ValueError) as context:
            player.bet()  # Should raise ValueError if no funds
        self.assertEqual(str(context.exception), "Player 1 has no funds to bet.")

    def test_receive_winnings(self):
        player = Player(1, 100)
        player.receive_winnings(50)
        self.assertEqual(player.funds, 150)  # Funds should increase by 50

class TestGame(unittest.TestCase):
    def test_game_initialisation(self):
        game = Game(2, 5)
        self.assertEqual(len(game.players), 2)  # Should initialise 2 players
        self.assertEqual(game.rounds, 5)
        self.assertEqual(len(game.deck.cards), 52)  # Deck should have 52 cards

    def test_play_round(self):
        game = Game(2, 1)
        result = game.play_round()
        self.assertTrue(result)  # Play round should return True if successful

    def test_round_display(self):
        game = Game(5, 2)  # Start game with 5 players and 2 rounds
        try:
            game.start_game()
        except Exception as e:
            self.fail(f"Error during start_game: {e}")
        
        self.assertTrue(True)  # Placeholder to pass the test if no exceptions are raised

if __name__ == '__main__':
    unittest.main()
