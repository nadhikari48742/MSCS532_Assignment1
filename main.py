"""
main.py

Run insertion sort (descending) on a sample list or user-provided input.
"""

from insertion_sort_desc import insertion_sort_desc


def parse_int_list(user_input: str):
    cleaned = user_input.strip().replace("[", "").replace("]", "").replace(",", " ")
    parts = [p for p in cleaned.split() if p]
    return [int(p) for p in parts]


def main():
    print("Insertion Sort (Monotonically Decreasing Order)")
    print("Enter numbers separated by spaces or commas (or press Enter to use a default list).")

    user_input = input("Numbers: ").strip()
    if user_input:
        arr = parse_int_list(user_input)
    else:
        arr = [5, 2, 4, 6, 1, 3]

    print("\nOriginal:", arr)
    insertion_sort_desc(arr)
    print("Sorted (desc):", arr)


if __name__ == "__main__":
    main()
