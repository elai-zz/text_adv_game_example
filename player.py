# -*- coding: utf8 -*-

from collections import Counter
import items, world

class Player():
	def __init__(self):
		self.inventory = []
		self.location_x, self.location_y = world.starting_position
		self.states = []
		self.victory = False

	def print_inventory(self):
		if self.inventory == []:
			print "N/A"
		else:
			print "Here are your items:"
			print
			for item in self.inventory:
				print "\t" + item.name
			print

	def has_state(self, state):
		for player_state in self.states:
			if state == player_state:
				return True
		return False

	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		if action_method:
			action_method(**kwargs)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_west(self):
		self.move(dx=-1, dy=0)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_to(self, x, y):
		self.location_x = x
		self.location_y = y
		print(world.tile_exists(self.location_x, self.location_y).intro_text())

	def move_to_office(self):
		self.move_to(10, 10)

	def leave_work(self):
		self.move_to(0, 2)

	def leave_apt(self):
		self.move_to(5, 0)

	def move(self, dx, dy):
		self.location_x += dx
		self.location_y += dy
		print(world.tile_exists(self.location_x, self.location_y).intro_text())

	def solve(self):
		message = raw_input('Insert input')
		lower_case_msg = message.lower()
		
		if lower_case_msg == "answer":
			self.victory = True
			print """
			You Win.
			"""
		else:
			print """
			You don't win.
			"""

	def cook(self):
		for item in self.inventory:
			if isinstance(item, items.Potato):
				item.cook()

	def dial_phone(self):
		number = raw_input('Please enter Hawthorne\'s number: ')
		sanitized_number = "".join([d for d in number if d.isdigit()])
		if sanitized_number == "number":
			print """
			Correct"""
			self.move_to(20, 20)
		else:
			print """
			Incorrect.
			"""

	def play(self):
		print """
		Description here.
		"""
		for item in self.inventory:
			if isinstance(item, items.Baseball):
				third_puzzle_clue = items.PuzzleClueThree()
				self.inventory.remove(item)
				self.inventory.append(third_puzzle_clue)
				self.states.append("third_note")

				print """
		Description here.
		"""

	def clean_clothes(self):
		self.room.dirty = False
		self.inventory.append(items.PuzzleClueOne())
		self.states.append("first_note")
		print """ 
		Description here.
		"""

	def enter_work(self):
		if self.has_state("state"):
			self.move_to_office()
		else:
			print """ 
			Description here.
			"""

	def get_drunk(self):
		self.states.append("state")
		print """ 
		Description here.
		"""

	def view_first_note(self):
		print """
		Note1"""

	def view_second_note(self):
		print """
		Note 2"""

	def view_third_note(self):
		print """
		Note 3"""