
# Objective Function
def objective(x):
    """
    Objective function: f(x) = -(x - 3)^2 + 9
    The global maximum occurs at x = 3 with value f(3) = 9.
    """
    return -(x - 3) ** 2 + 9


# Hill Climbing Algorithm
def hill_climbing(start):
    """
    Simple Hill Climbing algorithm that moves to a
    neighboring state with a higher objective value.
    """
    current = start
    step = 0

    print(f"Initial State: x = {current}, f(x) = {objective(current)}")

    while True:
        step += 1

        left = current - 1
        right = current + 1

        current_value = objective(current)
        left_value = objective(left)
        right_value = objective(right)

        print(
            f"Step {step}: Current x={current} (f={current_value}) | "
            f"Left x={left} (f={left_value}) | "
            f"Right x={right} (f={right_value})"
        )

        # Find the better neighbor
        if left_value > current_value:
            current = left
        elif right_value > current_value:
            current = right
        else:
            return current, current_value


# Main Program
if __name__ == "__main__":
    start = 0

    print("Hill Climbing Optimization:")
    print("Objective: Maximize f(x) = -(x - 3)^2 + 9")

    best_state, best_value = hill_climbing(start)

    print()
    print("Optimized Result:")
    print("  Best State (x):", best_state)
    print("  Best Value f(x):", best_value)
