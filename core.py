import random

class Game:
    """Class representing a game instance."""
    def __init__(self, name: str, max_players: int) -> None:
        """Initialize the game with a name and max players."""
        self.name = name
        self.max_players = max_players
        self.players = []

    def add_player(self, player_name: str) -> bool:
        """Add a player to the game if not full."""
        if len(self.players) < self.max_players:
            self.players.append(player_name)
            return True
        return False

    def start_game(self) -> str:
        """Start the game if enough players are present."""
        if len(self.players) < 2:
            return "Not enough players to start the game."
        return f"{self.name} has started with players: {', '.join(self.players)}"

    def end_game(self) -> str:
        """End the game and return a summary of players."""
        return f"Game {self.name} ended. Players: {', '.join(self.players)}"

    def get_random_winner(self) -> str:
        """Select and return a random winner from the players."""
        if not self.players:
            return "No players in the game."
        return random.choice(self.players)