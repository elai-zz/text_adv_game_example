class Item:
	"""Base class for all items"""
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return self.name + " : " + self.description + ", " + self.value

class Potato(Item):
	def __init__(self):
		Item.__init__(self, "Potato", "Description", 1)
		self.state = "raw"

	def cook(self):
		self.state = "Cooked"
		self.value += 1
		print """
		You walked over to the kitchen and you cooked the potato.
		"""

class MinnaHair(Item):
	def __init__(self):
		Item.__init__(self, "Minna hair", "Description", -1)

class DirtyClothes(Item):
	def __init__(self):
		Item.__init__(self, "Dirty clothes", "Description", -10)

class PuzzleClueOne(Item):
	def __init__(self):
		Item.__init__(self, "Note 1", "Description", 1000)

class PuzzleClueTwo(Item):
	def __init__(self):
		Item.__init__(self, "Note 2", "Description", 1000)

class Dollar(Item):
	def __init__(self):
		Item.__init__(self, "Dollar Bill", "Description", 1)

class PuzzleClueThree(Item):
	def __init__(self):
		Item.__init__(self, "Note 3", "Description", 1000)

class Baseball(Item):
	def __init__(self):
		Item.__init__(self, "Baseball", "Description", 10)