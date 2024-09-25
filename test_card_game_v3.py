import unittest
from card_game_v3 import Card, Deck, Player, Game

class TestCard(unittest.TestCase):
    def test_card_initialisation(self):
        """Test initialisation of a card with valid suit and value."""
        card = Card('Hearts', 'King')
        self.assertEqual(card.suit, 'Hearts')
        print(f"Card suit initialisation passed: {card.suit}")
        self.assertEqual(card.value, 'King')
        print(f"Card value initialisation passed: {card.value}")

    def test_get_value(self):
        """Test getting the value of a valid card."""
        card = Card('Diamonds', 'Ace')
        self.assertEqual(card.get_value(), 14)  # Ace should return 14
        print("Getting value for Ace passed.")

    def test_invalid_card_value(self):
        """Test that an error is raised for invalid card values."""
        with self.assertRaises(ValueError) as context:
            Card('Hearts', '17')  # 17 is not a valid card value
        self.assertEqual(str(context.exception), "Invalid card value: 17. Must be one of ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'].")
        print("Invalid card value test passed.")

class TestDeck(unittest.TestCase):
    def test_deck_initialisation(self):
        """Test that the deck is initialised with 52 cards."""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)  # Should have 52 cards initially
        print("Deck initialisation test passed with 52 cards.")

    def test_shuffle(self):
        """Test that the deck is shuffled."""
        deck = Deck()
        original_order = deck.cards.copy()
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_order)  # The deck should be shuffled
        print("Deck shuffle test passed; order has changed.")

    def test_deal(self):
        """Test that dealing a card decreases the deck size."""
        deck = Deck()
        top_card = deck.deal()
        self.assertEqual(len(deck.cards), 51)  # Should have one less card after dealing
        self.assertIsInstance(top_card, Card)  # The dealt card should be an instance of Card
        print(f"Dealing a card test passed; dealt {top_card}.")

class TestPlayer(unittest.TestCase):
    def test_player_initialisation(self):
        """Test the initialisation of a player."""
        player = Player(1, 100)
        self.assertEqual(player.id, 1)
        print(f"Player initialisation test passed with ID: {player.id}")
        self.assertEqual(player.funds, 100)
        print(f"Player funds initialisation test passed with funds: {player.funds}")

    def test_bet(self):
        """Test the bet function of a player."""
        player = Player(1, 100)
        bet_amount = player.bet()
        self.assertEqual(bet_amount, 1)  # Bet should be 1
        print(f"Bet function test passed; bet amount: {bet_amount}")
        self.assertEqual(player.funds, 99)  # Funds should decrease by 1
        print(f"Funds after bet test passed; remaining funds: {player.funds}")

    def test_bet_no_funds(self):
        """Test betting when the player has no funds."""
        player = Player(1, 0)
        with self.assertRaises(ValueError) as context:
            player.bet()  # Should raise ValueError if no funds
        self.assertEqual(str(context.exception), "Player 1 has no funds to bet.")
        print("Bet with no funds test passed; error raised as expected.")

    def test_receive_winnings(self):
        """Test receiving winnings by a player."""
        player = Player(1, 100)
        player.receive_winnings(50)
        self.assertEqual(player.funds, 150)  # Funds should increase by 50
        print(f"Receiving winnings test passed; updated funds: {player.funds}")

class TestGame(unittest.TestCase):
    def test_game_initialisation(self):
        """Test initialisation of the game with players and a deck."""
        game = Game(2, 5)
        self.assertEqual(len(game.players), 2)  # Should initialise 2 players
        print("Game initialisation test passed with 2 players.")
        self.assertEqual(game.rounds, 5)
        print(f"Game rounds initialisation test passed; rounds: {game.rounds}")
        self.assertEqual(len(game.deck.cards), 52)  # Deck should have 52 cards
        print("Game initialisation test passed; deck has 52 cards.")

    def test_play_round(self):
        """Test playing a round of the game."""
        game = Game(2, 1)
        result = game.play_round()
        self.assertTrue(result)  # Play round should return True if successful
        print("Play round test passed; round played successfully.")

    def test_round_display(self):
        """Test the round display functionality."""
        game = Game(5, 2)  # Start game with 5 players and 2 rounds
        try:
            game.start_game()
        except Exception as e:
            self.fail(f"Error during start_game: {e}")
        
        self.assertTrue(True)  # Placeholder to pass the test if no exceptions are raised
        print("Round display test passed; no exceptions raised during game start.")

if __name__ == '__main__':
    unittest.main()
