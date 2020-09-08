"""Quick sort algorithm"""

import logging
import random

def quick_sort(arr, start, end):

    # End when start index is >= end (smallest partition has been sorted)
    if start >= end:
        return

    # Pick a pivot value, swap other values in list around that value, return its index
    p = _partition(arr, start, end)

    # Now do the same thing recursively for the left and right sub-lists around the pivot index, returns when start>=end
    quick_sort(arr, start, p - 1)
    quick_sort(arr, p + 1, end)


def _partition(arr, start, end):
    logging.debug(f"Start, End ({start},{end}). Partitioning array: {arr}")

    # Pick a "pivot" value around which to swap other values in this partition. In this case we just pick first value

    pivot = arr[start]

    logging.debug(f"Pivot value: {pivot} at index: {start}")

    # Start looking for other out of order values to swap
    low = start + 1
    high = end
    logging.debug(f"Low, High ({low}, {high}). Looking for out-of-order values to swap...")

    # While other values in list are out of order around this pivot value
    while True:

        # Find out-of-order high value to the right of pivot (if other value is less than)
        while low <= high and arr[high] >= pivot:
            logging.debug(f"Value ({arr[high]}) at index {high} is in order, moving high to left (-1)...")
            high -= 1

        # Find out-of-order low value to the left of pivot (if other value is greater than)
        while low <= high and arr[low] <= pivot:
            logging.debug(f"Value ({arr[low]}) at index {low} is in order, moving low to right (+1)...")
            low += 1

        # Found two values that are out-of-order, now swap them so that they are in order
        if low < high:
            logging.debug(f"Found two out-of-order values to swap. Low value: {arr[low]} at index: {low}, with high value: {arr[high]} at index: {high}")
            arr[low], arr[high] = arr[high], arr[low]

        # We have swapped all out-of-order values, this arr is now partitioned into "correct" order (in terms of greater/less than the pivot)
        else:
            logging.debug(f"Found all out-of-order values to swap. This arr is now partitioned correctly around pivot: {arr}")
            break

    # Done sorting this partition, return index of partition
    logging.debug(f"Finished partitioning values, swapping pivot value ({arr[start]}) into correct position at index ({high})")
    arr[start], arr[high] = arr[high], arr[start]

    logging.debug(f"In order array for this partition: {arr}")
    logging.debug(f"Returning partition index: {high}")

    return high







if __name__ == "__main__":

    # Default INFO. Set to DEBUG to see inner working on quick sort
    logging.basicConfig(level='DEBUG')

    # # Hardcoded test
    # arr = [10, 7, 8, 9, 1, 5]
    # quick_sort(arr, 0, len(arr)-1)
    #
    # logging.info("Sorted array is:")
 


    # Automated tests
    num_tests = 1
    min_array_size = 4
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

        # Now use our quick sort implementation
        quick_sort(unsorted_array_copy, 0 , len(unsorted_array_copy)-1)


        logging.debug(f"Default sorted array {i}: {unsorted_array}")
        logging.debug(f"Quick sorted array {i}: {unsorted_array_copy}")

        # Compare to see if our quick sort implementation worked
        if unsorted_array == unsorted_array_copy:
            logging.info(f"Array {i} sorted correctly! {unsorted_array_copy}")
        else:
            logging.error(f"ERROR: Array {i} NOT sorted correctly! {unsorted_array_copy}")
            tests_passed = False


    logging.info(f"Result of all tests: {tests_passed}")