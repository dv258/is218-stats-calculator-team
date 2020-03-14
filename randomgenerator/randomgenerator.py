import random


class RandomGenerator:
	def __init__(self):
		pass

	"""returns a random number betweeen [x, y), returns an integer if both ranges are integers"""
	@staticmethod
	def range(x, y):
		if type(x) == int and type(y) == int:
			return random.randrange(x, y)

		return random.random() * (y - x) + x

	@staticmethod
	def rangeSeeded(seed, x, y):
		random.seed(seed)

		return RandomGenerator.range(x, y)

	@staticmethod
	def rangeListSeeded(seed, n, x, y):
		data = []
		for i in range(n):
			data.append(RandomGenerator.range(x, y))

		return data

	@staticmethod
	def choose(data):
		return data[RandomGenerator.range(0, len(data))]

	@staticmethod
	def chooseN(data, n):
		choices = []
		for x in range(n):
			choices.append(RandomGenerator.choose(data))

		return choices

	@staticmethod
	def chooseNSeeded(data, seed, n):
		random.seed(seed)

		return RandomGenerator.chooseN(data, n)
