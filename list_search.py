# ============================================================
# also searches for a target element and returns its index.
# ============================================================

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
    print("             SEARCHING ON LIST")
    print("=" * 19 + "By Tajir Ramadhan" + "=" * 19)

    integer_list = [34, 7, 23, 32, 5, 62, 19, 45, 11, 28]
    print(f"\n  List: {integer_list}")

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

    print("=" * 22 + "THE END" + "=" * 22)


if __name__ == "__main__":
    main()
