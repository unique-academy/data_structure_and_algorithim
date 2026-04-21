# Demonstrates creating and modifying a list of integers
# using append(), insert(), remove(), and pop()

def display_list(label, data):
    """Custom function to print a labeled list."""
    print(f"  {label}: {data}")


def main():
    print("=" * 55)
    print("       LIST OPERATIONS: INSERT, DELETE, MODIFY")
    print("=" * 19 + "By Tajir Ramadhan" + "=" * 19)

    # --- 1. CREATE ---
    integer_list = [100, 200, 300, 400, 500]
    display_list("Initial list", integer_list)

    # --- 2. APPEND fuction adds the value to the end ---
    integer_list.append(600)
    display_list("After append(600)", integer_list)

    # --- 3. INSERT() add at a specific defined index ---
    integer_list.insert(2, 250)          # Insert 250 at index 2
    display_list("After insert(2, 250)", integer_list)

    # --- 4. MODIFY() change an element by index ---
    integer_list[0] = 50                # Replace 100 with 50
    display_list("After modifying index 0 → 50", integer_list)

    # --- 5. REMOVE() delete first occurrence of a value ---
    integer_list.remove(400)
    display_list("After remove(400)", integer_list)

    # --- 6. POP() remove and return element at index ---
    popped_value = integer_list.pop(3)  # Remove element at index 3
    display_list(f"After pop(3)  [popped: {popped_value}]", integer_list)

    # --- 7. SORT ---
    integer_list.sort()
    display_list("After sort()", integer_list)

    print("=" * 22 + "THE END" + "=" * 22)


if __name__ == "__main__":
    main()
