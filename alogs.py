
"""
Darius Jones
5/22/2018
Useful Algorithms Implemented in Python

"""
import random

# Binary Search, very fast and useful
# O(log n) -> log base 2 number of elements

def binary_search(list, item):
	low = 0
	high = len(list)-1

	while low <= high:
		mid = low + ((high - low) / 2)
		guess = list[mid]

		if guess == item:
			return mid
		if guess > mid:
			high = mid - 1
		else:
			low = mid + 1
	return None

# Implement a recusive version

# Selection Sort
# O(n) -> very slow

def findSamallest(array):
	smallest = array[0]
	smallestIndex = 0

	for index in range(1, len(array)):
		if array[index] < smallest:
			smallest = array[index]
			smallestIndex = index

	return smallestIndex

def selectionSort(array):
	newArray = []
	for index in range(len(array)):
		smallest = findSamallest(array)
		newArray.append(array.pop(smallest))
	return newArray

# Quick Sort
# worst-case O(n) best-case O(log n) because of the pivot[randomly picked]
def quickSort(array):

	if len(array) < 2:
		return array
	else:
		pivot = random.choice(array)
		lessThanPivot = [index for index in array if index < pivot]
		equalToPivot = [index for index in array if index == pivot]
		greaterThanPivot = [index for index in array if index > pivot]
		return quickSort(lessThanPivot) + equalToPivot + quickSort(greaterThanPivot)

# Breadth-first search
