"""
test_insertion_sort.py

Basic tests for insertion_sort_desc using plain asserts.
Run python test_insertion_sort.py
"""

from insertion_sort_desc import insertion_sort_desc


def test_basic():
    arr = [5, 2, 4, 6, 1, 3]
    insertion_sort_desc(arr)
    assert arr == [6, 5, 4, 3, 2, 1]


def test_already_sorted_desc():
    arr = [9, 7, 7, 2, 1]
    insertion_sort_desc(arr)
    assert arr == [9, 7, 7, 2, 1]


def test_sorted_asc_to_desc():
    arr = [1, 2, 3, 4]
    insertion_sort_desc(arr)
    assert arr == [4, 3, 2, 1]


def test_duplicates():
    arr = [3, 1, 2, 3, 2]
    insertion_sort_desc(arr)
    assert arr == [3, 3, 2, 2, 1]


def test_empty_and_single():
    arr1 = []
    insertion_sort_desc(arr1)
    assert arr1 == []

    arr2 = [42]
    insertion_sort_desc(arr2)
    assert arr2 == [42]


def run_all_tests():
    test_basic()
    test_already_sorted_desc()
    test_sorted_asc_to_desc()
    test_duplicates()
    test_empty_and_single()
    print("All tests passed ✅")


if __name__ == "__main__":
    run_all_tests()
