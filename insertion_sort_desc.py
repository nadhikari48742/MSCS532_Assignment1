"""
insertion_sort_desc.py

Insertion Sort that sorts a list in monotonically decreasing order.

Course: MSCS 532
"""

from typing import List


def insertion_sort_desc(arr: List[int]) -> List[int]:
    """
    Sorts arr in-place in monotonically decreasing order using insertion sort.

    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        # For decreasing order, shift elements that are < key to the right
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1

        arr[i + 1] = key

    return arr


if __name__ == "__main__":
    # Quick demo if you run this file directly
    sample = [5, 2, 4, 6, 1, 3]
    print("Original:", sample)
    insertion_sort_desc(sample)
    print("Sorted (desc):", sample)
