"""Quick sort algorithm"""

import logging
import random


def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left = arr[:mid]  # Dividing the array elements
        right = arr[mid:]  # into 2 halves

        merge_sort(left)  # Sorting the first half
        merge_sort(right)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1



if __name__ == "__main__":

    # Default INFO. Set to DEBUG to see inner working on quick sort
    logging.basicConfig(level='DEBUG')

    # Automated tests
    num_tests = 1
    min_array_size = 5
    max_array_size = 5
    tests_passed = True
    for i in range(num_tests):

        # Create a random array of random size
        unsorted_array = []
        unsorted_array_size = random.randint(min_array_size, max_array_size)

        for n in range(unsorted_array_size):
            unsorted_array.append(random.randint(0, 100))

        unsorted_array_copy = unsorted_array.copy()
        logging.debug(f"Unsorted array {i}: {unsorted_array}")

        # Use built in sort for a reference
        unsorted_array.sort()

        # Now use our merge sort implementation
        merge_sort(unsorted_array_copy)

        logging.debug(f"Default sorted array {i}: {unsorted_array}")
        logging.debug(f"Merge sorted array {i}: {unsorted_array_copy}")

        # Compare to see if our quick sort implementation worked
        if unsorted_array == unsorted_array_copy:
            logging.info(f"Array {i} sorted correctly! {unsorted_array_copy}")
        else:
            logging.error(f"ERROR: Array {i} NOT sorted correctly! {unsorted_array_copy}")
            tests_passed = False

    logging.info(f"Result of all tests: {tests_passed}")