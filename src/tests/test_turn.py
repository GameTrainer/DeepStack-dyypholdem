
import settings.arguments as arguments
import settings.constants as constants

import game.card_tools as card_tools
import game.card_to_string_conversion as card_to_string
from tree.tree_node import TreeNode


def prepare_test():

    current_node = TreeNode()

    current_node.board = card_to_string.string_to_board('3c5h4h3h')
    current_node.street = 3
    current_node.current_player = constants.Players.P2
    current_node.bets = arguments.Tensor([600, 600])
    current_node.num_bets = 0

    # current_node.board = card_to_string.string_to_board('Ts8c6hAs')
    # current_node.street = 3
    # current_node.current_player = constants.Players.P2
    # current_node.bets = arguments.Tensor([2700, 900])
    # current_node.num_bets = 1

    arguments.logger.debug(f"Board={card_to_string.cards_to_string(current_node.board)}, bets=({current_node.bets[0]}, {current_node.bets[1]})")

    player_range = card_tools.get_file_range('tests/ranges/situation3-p2.txt')
    opponent_range = card_tools.get_file_range('tests/ranges/situation3-p1.txt')

    player_range_tensor = arguments.Tensor(1, player_range.size(0))
    opponent_range_tensor = arguments.Tensor(1, opponent_range.size(0))

    # ranges from file
    player_range_tensor[0].copy_(player_range)
    opponent_range_tensor[0].copy_(opponent_range)

    # random/uniform ranges
    # player_range_tensor[0].copy_(card_tools.get_uniform_range(current_node.board))
    # opponent_range_tensor[0].copy_(card_tools.get_uniform_range(current_node.board))

    return current_node, player_range_tensor, opponent_range_tensor
