def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    #raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    else: 
        raise ValueError("Invalid difficulty level") #Claude AI (Agent Mode): Suggested ValueError to raise when no difficulties are recognized


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    #raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"  #Claude AI: Chat recognized bug and helped switch statements 
        if guess < secret:
            return "Too Low",  "📈 Go HIGHER!"  #Claude AI: Chat recognized bug and helped switch statements 
    except TypeError:
        g = int(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!" #Claude AI: Chat recognized bug and helped switch statements 
        if g < secret: 
            return "Too Low", "📈 Go HIGHER!"  #Claude AI: Chat recognized bug and helped switch statements 


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
