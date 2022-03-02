"""Practice making dictionary functions."""

__author__ = "730388033"


def invert(a_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, invert returns a dictionary with inverted keys and their values."""
    inverted_dict: dict[str, str] = dict()
    for key in a_dict:
        if a_dict[key] in inverted_dict:
            raise KeyError("whoops same key.")
        inverted_dict[a_dict[key]] = key
    return inverted_dict


def favourite_colour(initial_dict: dict[str, str]) -> str:
    """Given a dict of names and favourite colours, it returns the most frequent colour."""
    colour_dict: dict[str, int] = dict()
    for key in initial_dict:
        # colour_dict[initial_dict[key]] = key
        # for colour in colour_dict:
        #     if colour in colour_dict:
        #         colour_dict[colour] += 1
        #     else:
        #         colour_dict[colour] = 1
        colour = initial_dict[key]
        if colour in colour_dict:
            colour_dict[colour] += 1
        else:
            colour_dict[colour] = 1
    return max(colour_dict)
    

def main() -> None:
    """Start of fave colour."""
    colour_dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    print(favourite_colour(colour_dict))


def count(a_list: list[str]) -> dict[str, int]:
    """Given a list, each key with a unique value will be associated with a count of how many times its in the list."""
    count_dict: dict[str, int] = dict()
    for item in a_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


if __name__ == "__main__":
    main()