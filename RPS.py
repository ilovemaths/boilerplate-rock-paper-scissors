def player(prev_play, opponent_history=[]):
    # Add the opponent's last move to the history
    opponent_history.append(prev_play)

    # Implement multiple strategies based on opponent's history
    # You can use if-elif-else statements to choose the strategy
    # For example, check if opponent's last move was "R", "P", or "S"

    # Strategy 1: Always play "R" on the first move
    if prev_play == "":
        return "R"

    # Strategy 2: Counter the opponent's last move
    # This strategy can be based on the opponent's last move
    # For example, if the opponent played "R" last, play "P" to counter it

    # Strategy 3: Random move
    # You can also include a random strategy to introduce variability
    # For example, generate a random move ("R", "P", or "S") if no specific strategy applies

    # You can combine multiple strategies or create more complex logic
    # depending on your observations of the opponent's behavior

    # Finally, return the chosen move
    return chosen_move
