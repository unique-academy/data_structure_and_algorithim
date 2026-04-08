# ============================================================
# Reverses a list manually — without reverse() or slicing.
# Two approaches are shown: in-place two-pointer swap and
# building a new reversed list.
# ============================================================


def reverse_inplace(numbers):
    """
    Reverse the list IN PLACE using the two-pointer technique.
    left pointer starts at index 0, right pointer at the last index.
    They swap elements and move toward the centre until they meet.
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        # Swap elements at left and right positions
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1    # Move left pointer rightward
        right -= 1   # Move right pointer leftward

    return numbers


def reverse_new_list(numbers):
    """
    Return a NEW reversed list by iterating from the last index
    to index 0.
    """
    reversed_list = []
    for index in range(len(numbers) - 1, -1, -1):
        reversed_list.append(numbers[index])
    return reversed_list


def main():
    print("=" * 55)
    print("                MANUAL LIST REVERSAL")
    print("=" * 19 + "By Tajir Ramadhan" + "=" * 19)

    # --- Approach 1: In-place two-pointer swap ---
    original = [10, 20, 30, 40, 50, 60, 70]
    print(f"\n  Original list        : {original}")

    reverse_inplace(original)
    print(f"  In-place reversed    : {original}")

    # --- Approach 2: Build a new reversed list ---
    source = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"\n  Source list          : {source}")
    reversed_copy = reverse_new_list(source)
    print(f"  New reversed list    : {reversed_copy}")
    print(f"  Source unchanged     : {source}")   # Confirm original is intact


    print("=" * 22 + "THE END" + "=" * 22)


if __name__ == "__main__":
    main()
