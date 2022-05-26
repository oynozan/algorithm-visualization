from random import shuffle #For Bogo Algorithm

class Algorithms:
	def __init__(self):
		print("Hello World")

	#Bubble Sorting Algorithm
	def BubbleSort(self, arr):
		for i in range(len(arr) - 1):
			if arr[i] > arr[i+1]:
				self.tempVal = arr[i+1]
				arr[i+1] = arr[i]
				arr[i] = self.tempVal

		return arr

	#Most useless Algorithm (but my favourite): Bogo Sorting
	def BogoSort(self, arr):
		for i in range(len(arr) - 1):
			if arr[i] > arr[i+1]:
				shuffle(arr)
				return arr
		return arr