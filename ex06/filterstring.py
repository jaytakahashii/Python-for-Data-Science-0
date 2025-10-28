import sys
from ft_filter import ft_filter


def long_enough(word: str, n: int) -> bool:
    """Checks if a word's length is at least n."""
    return len(word) > n


if __name__ == "__main__":
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
