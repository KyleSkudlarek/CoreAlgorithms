import random

"""Quick sort algorithm"""

def quick_sort(arr, start, end):

    # print(f"Sorting array: {arr}")
    # print(f"Start: {start}, End: {end}")

    if start >= end:
        return

    p = _partition(arr, start, end)

    # print("Partition p: " + str(p))

    quick_sort(arr, start, p - 1)
    quick_sort(arr, p + 1, end)


def _partition(arr, start, end):

    if start < len(arr)-1:

        # print(f"Partitioning array: {arr}")

        pivot = arr[start]

        # print(f"Pivot value: {pivot}")

        low = start + 1
        high = end

        # print(f"low, high ({low},{high})")

        # While value are out of order for this pivot value
        while True:

            # Find out-of-order value to the right of pivot
            while low <= high and arr[high] >= pivot:
                # print(f"Value ({arr[high]}) at index {high} is in order, moving high to left (-1)...")
                high -= 1

            # print(f"Found an out-of-order value ({arr[high]}) at index {high}!")

            # Find out-of-order value to the left of pivot
            while low < high and arr[low] <= pivot:
                # print(f"Value ({arr[low]}) at index {low} is in order, moving low to right (+1)...")
                low += 1

            # print(f"Found an out-of-order value ({arr[low]}) at index {low}!")


            # Found two values that are out-of-order, swap
            if low < high:
                # print(f"Found two out-of-order values to swap: {arr[low]}, {arr[high]}")
                arr[low], arr[high] = arr[high], arr[low]

            # We have swapped all out-of-order values
            else:
                break

        # Done sorting this partition, return index of partition
        # print(f"Findished swapping all out-of-order values, putting pivot value ({arr[start]}) into correct position at index ({high}),"
        #       f" and returning index...")

        arr[start], arr[high] = arr[high], arr[start]

        # print(f"In order array for this partition: {arr}")

        # print(f"Returning partition index: {high}")
        return high







if __name__ == "__main__":

    # # Hardcoded test
    # arr = [10, 7, 8, 9, 1, 5]
    # quick_sort(arr, 0, len(arr)-1)
    #
    # print("Sorted array is:")
    # print(arr)


    # Automated test
    num_tests = 200
    max_array_size = 10
    tests_passed = True
    for i in range(num_tests):

        # Create a random array of random size
        unsorted_array = []
        unsorted_array_size = random.randint(1, max_array_size)

        for n in range(unsorted_array_size):
            unsorted_array.append(random.randint(0, 100))

        unsorted_array_copy = unsorted_array.copy()
        #print(f"Unsorted array {i}: {unsorted_array}")

        unsorted_array.sort()
        #print(f"Default sorted array {i}: {unsorted_array}")

        quick_sort(unsorted_array_copy, 0 , len(unsorted_array_copy)-1)
        #print(f"Quick sorted array {i}: {unsorted_array_copy}")

        if unsorted_array == unsorted_array_copy:
            print(f"Array {i} sorted correctly!")
        else:
            print(f"ERROR: Array {i} NOT sorted correctly")
            tests_passed = False


    print(f"Result of all tests: {tests_passed}")