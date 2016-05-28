from player import Player
import items as Items

class Action:
	def __init__(self, method, name, **kwargs):
		self.method = method
		self.name = name
		self.kwargs = kwargs

	def __str__(self):
		return self.name

class MoveSouth(Action):
	def __init__(self):
		Action.__init__(self, method=Player.move_south, name='south')

class MoveNorth(Action):
	def __init__(self):
		Action.__init__(self, method=Player.move_north, name='north')

class MoveEast(Action):
	def __init__(self):
		Action.__init__(self, method=Player.move_east, name='east')

class MoveWest(Action):
	def __init__(self):
		Action.__init__(self, method=Player.move_west, name='west')

class ViewInventory(Action):
	def __init__(self):
		Action.__init__(self, method=Player.print_inventory, name='view')

class CookPotato(Action):
	def __init__(self):
		Action.__init__(self, method=Player.cook, name='cook potato')

class DoLaundry(Action):
	def __init__(self):
		Action.__init__(self, method=Player.clean_clothes, name='clean')

class EnterWork(Action):
	def __init__(self):
		Action.__init__(self, method=Player.enter_work, name='enter work')

class LeaveWork(Action):
	def __init__(self):
		Action.__init__(self, method=Player.leave_work, name='leave work')

class LeaveApt(Action):
	def __init__(self):
		Action.__init__(self, method=Player.leave_apt, name='leave apt')

class GetDrunk(Action):
	def __init__(self):
		Action.__init__(self, method=Player.get_drunk, name='drink')

class DialPhone(Action):
	def __init__(self):
		Action.__init__(self, method=Player.dial_phone, name='dial phone')

class Play(Action):
	def __init__(self):
		Action.__init__(self, method=Player.play, name='play')

class Solve(Action):
	def __init__(self):
		Action.__init__(self, method=Player.solve, name='answer Minna')

class ViewFirstNote(Action):
	def __init__(self):
		Action.__init__(self, method=Player.view_first_note, name='read note1')

class ViewSecondNote(Action):
	def __init__(self):
		Action.__init__(self, method=Player.view_second_note, name='read note2')

class ViewThirdNote(Action):
	def __init__(self):
		Action.__init__(self, method=Player.view_third_note, name='read note3')