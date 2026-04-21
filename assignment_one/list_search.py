# ============================================================
# Finds maximum, minimum, and sum of list elements;
# also searches for a target element and returns its index.
# ============================================================


# --------- Finding maximum of list ---------
def find_maximum(numbers):
    """Return the largest element without using max()."""
    if not numbers:
        return None
    current_max = numbers[0]
    # for number in numbers[1:]:
    #     if number > current_max:
    #         current_max = number
    """The memory efficient wat to handle this"""
    for i in range(1, len(numbers)):
        if numbers[i] > current_max:
            current_max = numbers[i]
    return current_max


# --------- Finding minimum of list ---------
def find_minimum(numbers):
    """Return the smallest element without using min()."""
    if not numbers:
        return None
    current_min = numbers[0]
    """Slicing approach for handling fetching, which is memory expensive due to copy"""
    for number in numbers[1:]:
        if number < current_min:
            current_min = number
    return current_min


# --------- Finding sum of list ---------
def calculate_sum(numbers):
    """Return the total of all elements without using sum()."""
    total = 0
    for number in numbers:
        total += number
    return total


# ---------- Search certain value----------

def linear_search(numbers, target):
    """
    Search for target in numbers using linear search.
    Returns the index if found, or -1 if not found.
    """
    for index, value in enumerate(numbers): #function that return index, value
        if value == target:
            return index
    return -1          # Sentinel value – not found


# ---------- Main ----------

def main():
    print("=" * 55)
    print("        LIST STATISTICS & SEARCH")
    print("=" * 19 + "By Tajir Ramadhan" + "=" * 19)

    integer_list = [34, 7, 23, 32, 5, 62, 19, 45, 11, 28]
    print(f"\n  List: {integer_list}")

    # Statistics part
    print("\n  --- Statistics Part ---")
    print(f"  Maximum : {find_maximum(integer_list)}")
    print(f"  Minimum : {find_minimum(integer_list)}")
    print(f"  Sum     : {calculate_sum(integer_list)}")

    # Search operation when element found
    print("\n  --- Search Part ---")
    target = 19
    result = linear_search(integer_list, target)
    if result != -1:
        print(f"  Element {target} found at index {result}.")
    else:
        print(f"  Element {target}: Not Found.")

    # Search operation element NOT present
    target_missing = 99
    result_missing = linear_search(integer_list, target_missing)
    if result_missing != -1:
        print(f"  Element {target_missing} found at index {result_missing}.")
    else:
        print(f"  Element {target_missing}: Not Found.")

    # Final case: empty list
    print("\n  Final case: statistics on empty list:")
    empty = []
    print(f"  Maximum : {find_maximum(empty)}")   # Returns None
    print(f"  Minimum : {find_minimum(empty)}")   # Returns None
    print(f"  Sum     : {calculate_sum(empty)}")  # Returns 0

    print("=" * 22 + "THE END" + "=" * 22)


if __name__ == "__main__":
    main()
