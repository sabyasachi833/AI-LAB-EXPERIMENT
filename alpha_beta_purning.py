
# Alpha-Beta Pruning Algorithm
def alpha_beta(node, depth, alpha, beta, maximizing_player):
    """
    Alpha-Beta Pruning Optimization for Minimax.
    alpha: Best value maximizer can guarantee so far.
    beta: Best value minimizer can guarantee so far.
    Prunes subtrees whenever alpha >= beta.
    """

    if depth == 0 or isinstance(node, int):
        return node

    if maximizing_player:
        best_value = float('-inf')

        for child in node:
            value = alpha_beta(child, depth - 1, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            if alpha >= beta:
                print(
                    f"  [Pruned at Maximizer] "
                    f"alpha ({alpha}) >= beta ({beta})"
                )
                break

        return best_value

    else:
        best_value = float('inf')

        for child in node:
            value = alpha_beta(child, depth - 1, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)

            if alpha >= beta:
                print(
                    f"  [Pruned at Minimizer] "
                    f"alpha ({alpha}) >= beta ({beta})"
                )
                break

        return best_value


# Main Program
if __name__ == "__main__":
    # Nested list game tree
    tree = [[3, 5], [2, 9]]

    alpha = float('-inf')
    beta = float('inf')

    print("Game Tree Structure:")
    print(" ", tree)
    print("Initial Alpha:", alpha, "| Initial Beta:", beta)

    print("\nTraversing Tree with Alpha-Beta Pruning:")

    result = alpha_beta(tree, 2, alpha, beta, True)

    print("Optimal Value:", result)
