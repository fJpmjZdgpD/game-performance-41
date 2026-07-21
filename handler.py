import json

class GameError(Exception):
    pass


def handle_game_error(error):
    response = {'status': 'error', 'message': str(error)}
    return json.dumps(response)


def process_game_action(action):
    try:
        if action not in ['start', 'stop', 'pause']:
            raise GameError('Invalid action')
        # Simulated processing logic goes here
        return json.dumps({'status': 'success', 'action': action})
    except GameError as e:
        return handle_game_error(e)
    except Exception as e:
        return handle_game_error(e)


if __name__ == '__main__':
    print(process_game_action('start'))  
    print(process_game_action('invalid_action'))  
    