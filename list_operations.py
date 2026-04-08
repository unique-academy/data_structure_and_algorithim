# ============================================================
# list_operations.py
# Demonstrates creating and modifying a list of integers
# using append(), insert(), remove(), and pop()
# ============================================================

def display_list(label, data):
    """Helper function to print a labelled list."""
    print(f"  {label}: {data}")


def main():
    print("=" * 55)
    print("       LIST OPERATIONS: INSERT, DELETE, MODIFY")
    print("=" * 55)

    # --- 1. CREATE ---
    integer_list = [10, 20, 30, 40, 50]
    display_list("Initial list", integer_list)

    # --- 2. APPEND – add to the end ---
    integer_list.append(60)
    display_list("After append(60)", integer_list)

    # --- 3. INSERT – add at a specific index ---
    integer_list.insert(2, 25)          # Insert 25 at index 2
    display_list("After insert(2, 25)", integer_list)

    # --- 4. MODIFY – change an element by index ---
    integer_list[0] = 5                 # Replace 10 with 5
    display_list("After modifying index 0 → 5", integer_list)

    # --- 5. REMOVE – delete first occurrence of a value ---
    integer_list.remove(40)
    display_list("After remove(40)", integer_list)

    # --- 6. POP – remove and return element at index ---
    popped_value = integer_list.pop(3)  # Remove element at index 3
    display_list(f"After pop(3)  [popped: {popped_value}]", integer_list)

    # --- 7. SORT ---
    integer_list.sort()
    display_list("After sort()", integer_list)

    # --- Edge case: pop from an empty list ---
    print("\n  Edge case – popping from empty list:")
    empty_list = []
    try:
        empty_list.pop()
    except IndexError:
        print("  IndexError caught: cannot pop from an empty list.")

    print("=" * 55)


if __name__ == "__main__":
    main()
