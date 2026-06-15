from typing import Dict, Any

class GameHandler:
    def __init__(self, game_data: Dict[str, Any]) -> None:
        self.game_data = game_data

    def start_game(self) -> None:
        print('Starting the game...')

    def pause_game(self) -> None:
        print('Game paused.')

    def resume_game(self) -> None:
        print('Resuming the game...')

    def end_game(self) -> None:
        print('Ending the game...')

    def get_game_status(self) -> str:
        return 'Game is currently running.'

# Example usage
if __name__ == '__main__':
    game = GameHandler({'level': 1, 'score': 0})
    game.start_game()
    print(game.get_game_status())
    game.pause_game()
    game.resume_game()
    game.end_game()