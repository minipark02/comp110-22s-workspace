"""Some examples of tender, loving function definitions."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repreats a loving message n times."""
    love_note: str = ""
    love_counter: int = 0
    while love_counter < n:
        love_note += love(to) + "\n"
        love_counter += 1
    return love_note