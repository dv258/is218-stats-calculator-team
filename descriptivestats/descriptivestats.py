import math


class DescriptiveStatistics:
	def __init__(self):
		pass

	@staticmethod	# data is a list of numbers Mean is the average of a set of numbers.
	def mean(data):
		if len(data) == 0:
			raise Exception("list is empty")

		return sum(data) / len(data)

	@staticmethod	# data is a list of numbers
	def median(data):
		if len(data) == 0:
			raise Exception("list is empty")

		sortedData = data[:]
		sortedData.sort()

		return DescriptiveStatistics._median(sortedData)["median"]

	@staticmethod	# data is a list of numbers Mode is the number which appears most often in a set of numbers
	def mode(data):
		if len(data) == 0:
			raise Exception("list is empty")

		count = {}
		maxCount = 0

		for d in data:
			if d not in count:
				count[d] = 0
			count[d] += 1

			if count[d] > maxCount:
				maxCount = count[d]

		if maxCount == 1:
			return []

		largest = []

		for k, v in count.items():
			if v == maxCount:
				largest.append(k)

		largest.sort()
		return largest

	"""sample standard deviation"""
	@staticmethod
	def stdev(data):	# data is a list of numbers The Standard Deviation is a measure of how spread out numbers are.
		if len(data) == 0:
			raise Exception("list is empty")
		if len(data) - 1 == 0:
			raise ZeroDivisionError()

		mean = DescriptiveStatistics.mean(data)
		total = 0

		for d in data:
			total += (d - mean) ** 2

		return math.sqrt(total / (len(data) - 1))

	"""population standard deviation"""
	@staticmethod
	def pstdev(data):	# data is a list of numbers
		if len(data) == 0:
			raise Exception("list is empty")

		mean = DescriptiveStatistics.mean(data)
		total = 0

		for d in data:
			total += (d - mean) ** 2

		return math.sqrt(total / len(data))

	"""sample variance"""
	@staticmethod
	def variance(data):	# data is a list of numbers The Variance is defined as: The average of the squared differences from the Mean.
		if len(data) == 0:
			raise Exception("list is empty")

		return DescriptiveStatistics.stdev(data) ** 2

	"""sample covariance"""
	@staticmethod	# data1 is a list of numbers and data2 is another list of numbers
	def covariance(data1, data2):
		if len(data1) == 0 or len(data2) == 0:
			raise Exception("list is empty")
		if len(data1) - 1 == 0:
			raise ZeroDivisionError()

		mean1 = DescriptiveStatistics.mean(data1)
		mean2 = DescriptiveStatistics.mean(data2)

		total = 0
		for x, y in zip(data1, data2):
			total += (x - mean1) * (y - mean2)

		return total / (len(data1) - 1)

	"""population covariance"""
	@staticmethod	# data1 is a list of numbers and data2 is another list of numbers Covariance is a measure of the joint variability of two random variables.
	def pcovariance(data1, data2):
		if len(data1) == 0:
			raise Exception("list is empty")

		mean1 = DescriptiveStatistics.mean(data1)
		mean2 = DescriptiveStatistics.mean(data2)

		total = 0
		for x, y in zip(data1, data2):
			total += (x - mean1) * (y - mean2)

		return total / len(data1)

	@staticmethod	# data is a list of numbers A quartile is defined as a group of values and/or means that divide a data set into quarters, or groups of four. 
	def quartiles(data):
		if len(data) == 0:
			raise Exception("list is empty")

		sortedData = data[:]
		sortedData.sort()

		quar2 = DescriptiveStatistics._median(sortedData)
		quar1 = DescriptiveStatistics._median(sortedData[:quar2["end1idx"] + 1])
		quar3 = DescriptiveStatistics._median(sortedData[quar2["start2idx"]:])

		return [quar1["median"], quar2["median"], quar3["median"]]

	@staticmethod	# data is a list of numbers
	def skewness(data):
		if len(data) == 0:
			raise Exception("list is empty")

		return 3 * (DescriptiveStatistics.mean(data) - DescriptiveStatistics.median(data)) / DescriptiveStatistics.stdev(data)

	@staticmethod
	def zscore(value, mean, stdev):
		if stdev == 0:
			raise ZeroDivisionError()

		return (value - mean) / stdev

	@staticmethod	# data1 is a list of numbers and data2 is another list of numbers
	def meanDeviation(data):
		if len(data) == 0:
			raise Exception("list is empty")

		mean = DescriptiveStatistics.mean(data)
		absdiff = []

		for d in data:
			absdiff.append(abs(d - mean))

		return DescriptiveStatistics.mean(absdiff)

	@staticmethod	# data1 is a list of numbers and data2 is another list of numbers
	def sampleCorrelation(data1, data2):
		return DescriptiveStatistics.covariance(data1, data2) / (DescriptiveStatistics.stdev(data1) * DescriptiveStatistics.stdev(data2))

	@staticmethod	# data1 is a list of numbers and data2 is another list of numbers
	def populationCorrelation(data1, data2):
		return DescriptiveStatistics.pcovariance(data1, data2) / (DescriptiveStatistics.pstdev(data1) * DescriptiveStatistics.pstdev(data2))

	"""assumes data is a list of numbers that is already sorted"""
	@staticmethod # median is the median value of a range of values.
	def _median(data):
		mid = len(data) // 2

		end1idx = mid - 1

		if len(data) & 1 == 1:
			median = data[mid]
			start2idx = mid + 1
		else:
			median = (data[mid - 1] + data[mid]) / 2
			start2idx = mid

		return {
			"median": median,
			"end1idx": end1idx,
			"start2idx": start2idx
		}
