from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """
    Search for the target element in a sorted array using binary search.
    :param arr: A sorted list of elements.
    :param target: The element to search for.
    :return: The index of the target element, or -1 if it is not found.
    """
    left, right = 0, len(arr) - 1  # Define left and right pointers to the beginning and end of the list.
    while left <= right:  # Keep searching until the pointers cross.
        mid = (left + right) // 2  # Calculate the middle index.
        if arr[mid] == target:  # If the middle element is the target, we're done.
            return mid
        elif arr[mid] < target:  # If the middle element is less than the target, search the right half.
            left = mid + 1
        else:  # If the middle element is greater than the target, search the left half.
            right = mid - 1
    return -1  # If the target element is not found, return -1.
