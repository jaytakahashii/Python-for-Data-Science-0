import sys
from ft_filter import ft_filter


def long_enough(word: str, n: int) -> bool:
    """
    Check if the length of the word is greater than n.

    Args:
        word (str): The word to check.
        n (int): The length threshold.
    Returns:
        bool: True if the length of the word is greater than n,
              False otherwise.
    """
    return len(word) > n


def main():
    """ Main function to filter words based on length. """
    if len(sys.argv) != 3:
        raise SystemExit("AssertionError: the arguments are bad")

    S = sys.argv[1]
    N = sys.argv[2]
    try:
        assert N.isdigit()
        N = int(N)
    except AssertionError:
        raise SystemExit("AssertionError: the arguments are bad")

    words = S.split(" ")
    filtered_words = ft_filter(lambda word: long_enough(word, N), words)
    print(filtered_words)


if __name__ == "__main__":
    main()
