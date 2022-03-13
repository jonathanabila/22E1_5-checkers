import random
from collections import deque

previous_board = deque(maxlen=5)


def minimax(game, depth, max_player, player):
    """
    param board: Current state of the board.
    param depth: Maximum depth to explore, less make the game faster, but also less smart.
    param max_player: The player to maxime to move.
    """

    best_board = game.board

    player_function = max if max_player else min
    best_score = float("-inf") if max_player else float("inf")

    if depth == 0 or game.get_winner():
        return game.board.evaluate(), game

    for board in game.board.get_valid_boards(player):
        should_max_player = False if max_player else True
        evaluation, _ = minimax(game, depth - 1, should_max_player, player)
        player_eval = player_function(best_score, evaluation)

        # The AI is going to play the start of the game in the same way always if we don't add some
        # randomization to the evaluation.
        if player_eval == evaluation and (
            random.randint(0, 9) > 7
            or player_eval < best_score
            and max_player
            or player_eval > best_score
            and not max_player
        ):

            # Sometimes, we AI keep doing the same steps to not lose pieces, we need to stop that.
            previous_board.append(board)
            if previous_board.count(board) > 2:
                continue

            best_board = board
            best_score = evaluation

    return best_score, best_board
