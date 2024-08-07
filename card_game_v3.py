import random
import time

# Record the start time of the execution
start_time = time.time()

class Card:
    def __init__(self, suit, value):
        """
        Initialise a card with a suit and value.

        :param suit: The suit of the card (e.g., 'Hearts', 'Diamonds').
        :param value: The value of the card (e.g., '2', 'King').
        """
        self.suit = suit
        self.value = value

    def __repr__(self):
        """
        Return a string representation of the card.

        :return: A string in the format 'value of suit'.
        """
        return f"{self.value} of {self.suit}"

    def get_value(self):
        """
        Return the numerical value of the card for comparison purposes.

        :return: An integer representing the card's value.
        """
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                  'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
        return values[self.value]


class Deck:
    def __init__(self):
        """
        Initialise the deck and build it.
        """
        self.build_deck()

    def build_deck(self):
        """
        Build a standard deck of 52 cards.
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        """
        Shuffle the deck of cards in place.
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        Deal a card from the deck.

        :return: The top card from the deck.
        """
        return self.cards.pop()


class Player:
    def __init__(self, player_id, funds):
        """
        Initialise a player with a unique ID and starting funds.

        :param player_id: The unique identifier for the player.
        :param funds: The initial amount of funds the player has.
        """
        self.id = player_id
        self.funds = funds

    def bet(self):
        """
        Place a bet of 1 fund.

        :return: The amount bet (1).
        :raises ValueError: If the player has no funds to bet.
        """
        if self.funds <= 0:
            raise ValueError(f"Player {self.id} has no funds to bet.")
        self.funds -= 1
        return 1

    def receive_winnings(self, amount):
        """
        Add winnings to the player's funds.

        :param amount: The amount of winnings to be added.
        """
        self.funds += amount


class Game:
    def __init__(self, players, rounds):
        """
        Initialise the game with a list of players and a number of rounds.

        :param players: The number of players in the game.
        :param rounds: The number of rounds to be played.
        """
        self.players = [Player(i + 1, rounds) for i in range(players)]  # Initialise players with funds
        self.deck = Deck()  # Create a new deck of cards
        self.deck.shuffle()  # Shuffle the deck
        self.rounds = rounds  # Set the number of rounds

    def play_round(self):
        """
        Play a single round of the game.

        :return: True if the round was played successfully; False otherwise.
        """
        active_players = [player for player in self.players if player.funds > 0]
        
        # Check if there are at least two players with funds
        if len(active_players) < 2:
            print("Not enough players with funds to continue the game.")
            return False

        bets = {}
        highest_card = None
        round_winner = None

        # Process each active player
        for player in active_players:
            # Rebuild and shuffle the deck if it is empty
            if len(self.deck.cards) == 0:
                print("Reshuffling deck")
                self.deck.build_deck()
                self.deck.shuffle()

            try:
                player_bet = player.bet()  # Player places a bet
                bets[player.id] = player_bet  # Record the bet
            except ValueError as e:
                print(e)  # Handle case where player has no funds
                continue  # Skip to the next player

            card = self.deck.deal()  # Deal a card to the player
            print(f"Player {player.id} draws {card}")

            # Determine if this player has the highest card so far
            if highest_card is None or card.get_value() > highest_card.get_value():
                highest_card = card
                round_winner = player

        # Announce the round winner and update their funds
        if round_winner:
            print(f"Player {round_winner.id} wins this round with {highest_card}")
            round_winner.receive_winnings(sum(bets.values()))  # Winner gets all bets
        else:
            print("No winner this round.")

        return True

    def start_game(self):
        """
        Start the game and play all rounds.
        """
        for round_num in range(self.rounds):
            print(f"Round {round_num + 1}")
            if not self.play_round():  # Play a round and check if the game should continue
                break

        self.show_final_results()  # Show results after all rounds

    def show_final_results(self):
        """
        Display the final results of the game.
        """
        print("\nFinal Results:")
        winner = max(self.players, key=lambda p: p.funds)  # Determine the player with the most funds
        for player in self.players:
            print(f"Player {player.id} has {player.funds} funds")  # Display each player’s funds
        print(f"Player {winner.id} wins the game with {winner.funds} funds!")  # Announce the overall winner


def main():
    """
    Main function to initialise and start the game.
    """
    num_players = int(input("Enter number of players: "))
    
    deck_size = 52
    max_rounds = deck_size // num_players

    print(f"Maximum number of rounds that can be played with {num_players} players is {max_rounds}")

    rounds = int(input(f"Enter number of rounds (1 to {max_rounds}): "))
    if rounds > max_rounds:
        print(f"Adjusted number of rounds to maximum possible: {max_rounds}")
        rounds = max_rounds

    # Initialise the game with the number of players and rounds
    game = Game(num_players, rounds)
    game.start_game()


if __name__ == "__main__":
    main()
    
// print("Execution Time:  %s seconds." % (time.time() - start_time))
# Print the execution time of the script only during debugging
# print("Execution Time:  %s seconds." % (time.time() - start_time))
