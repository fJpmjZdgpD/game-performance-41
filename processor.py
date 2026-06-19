from typing import List, Dict

class GameProcessor:
    def __init__(self, players: List[str]) -> None:
        self.players = players
        self.scores: Dict[str, int] = {player: 0 for player in players}

    def update_score(self, player: str, points: int) -> None:
        if player in self.scores:
            self.scores[player] += points

    def get_scores(self) -> Dict[str, int]:
        return self.scores

    def reset_scores(self) -> None:
        self.scores = {player: 0 for player in self.players}

    def get_winner(self) -> str:
        return max(self.scores, key=self.scores.get)

# Example usage
if __name__ == '__main__':
    game = GameProcessor(['Alice', 'Bob', 'Charlie'])
    game.update_score('Alice', 10)
    game.update_score('Bob', 5)
    print(game.get_scores())
    print('Winner:', game.get_winner())