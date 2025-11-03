# ex09/ft_package/__init__.py

def count_in_list(list_to_search: list, item_to_count) -> int:
    """
    Counts the number of occurrences of an item in a list.

    Args:
        list_to_search (list): The list to search within.
        item_to_count: The item whose occurrences are to be counted.

    Returns:
        int: The number of times the item appears in the list.
             Returns 0 if list_to_search is not a list.
    """
    try:
        if not isinstance(list_to_search, list):
            # Handle the case where the input is not a list
            # For this exercise, we'll return 0 as a form of graceful exit
            # instead of raising a TypeError, ensuring no unhandled exception.
            print("Error: First argument must be a list.")
            return 0

        # Use the built-in count method for efficiency
        return list_to_search.count(item_to_count)
    except Exception as e:
        # Catch any unexpected errors during the process
        print(f"An unexpected error occurred: {e}")
        return 0


def main():
    """
    Main function to test the count_in_list function.
    """
    print("--- Test 1 ---")
    my_list = ["toto", "tata", "toto"]
    item = "toto"
    result = count_in_list(my_list, item)
    print(f"List: {my_list}, Item: {item} -> Count: {result}")  # Expected: 2

    print("\n--- Test 2 ---")
    my_list = ["toto", "tata", "toto"]
    item = "tutu"
    result = count_in_list(my_list, item)
    print(f"List: {my_list}, Item: {item} -> Count: {result}")  # Expected: 0

    print("\n--- Test 3: Error Handling (Not a list) ---")
    result = count_in_list("a string", "a")
    print(f"Input: 'a string', Item: 'a' -> Count: {result}")  # Expected: 0


if __name__ == "__main__":
    main()
