"""Quick sort algorithm"""

import logging
import random


def merge_sort2(values):
    logging.debug(f"Values: {values}")

    if len(values) > 1:

        m = len(values) // 2

        logging.debug(f"m: {m}")

        left = values[:m]
        right = values[m:]

        logging.debug(f"left: {left}")
        logging.debug(f"right: {right}")


        left = merge_sort2(left)
        right = merge_sort2(right)

        logging.debug(f"left after recurse: {left}")
        logging.debug(f"right after recourse: {right}")

        values = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                values.append(left[0])
                logging.debug(f"Values: {values}")
                left.pop(0)
            else:
                values.append(right[0])
                logging.debug(f"Values: {values}")
                right.pop(0)

        for i in left:
            values.append(i)
            logging.debug(f"Values: {values}")
        for i in right:
            values.append(i)
            logging.debug(f"Values: {values}")

    logging.debug(f"len values < 1, returning values: {values}")
    return values

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
        sorted_array_copy = merge_sort2(unsorted_array_copy)

        logging.debug(f"Default sorted array {i}: {unsorted_array}")
        logging.debug(f"Merge2 sorted array {i}: {sorted_array_copy}")

        # Compare to see if our quick sort implementation worked
        if unsorted_array == sorted_array_copy:
            logging.info(f"Array {i} sorted correctly! {sorted_array_copy}")
        else:
            logging.error(f"ERROR: Array {i} NOT sorted correctly! {sorted_array_copy}")
            tests_passed = False

    logging.info(f"Result of all tests: {tests_passed}")