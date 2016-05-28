import items, actions, world

class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.isVisited = False

	def intro_text(self):
		raise NotImplementedError()
 
	def modify_player(self, player):
	    self.isVisited = True

	def adjacent_moves(self):
		"""Returns all move actions for adjacent tiles."""
		moves = []
		if world.tile_exists(self.x + 1, self.y):
		    moves.append(actions.MoveEast())
		if world.tile_exists(self.x - 1, self.y):
		    moves.append(actions.MoveWest())
		if world.tile_exists(self.x, self.y - 1):
		    moves.append(actions.MoveNorth())
		if world.tile_exists(self.x, self.y + 1):
		    moves.append(actions.MoveSouth())
		return moves
 
	def available_actions(self, player):
		"""Returns all of the available actions in this room."""
		moves = self.adjacent_moves()
		if player.has_state("first_note"):
			moves.append(actions.ViewFirstNote())
		if player.has_state("second_note"):
			moves.append(actions.ViewSecondNote())
		if player.has_state("third_note"):
			moves.append(actions.ViewThirdNote())
		moves.append(actions.ViewInventory())
		return moves

class ItemRoom(MapTile):
	def __init__(self, x, y, item):
		self.item = item
		MapTile.__init__(self, x, y)

	def add_item(self, player):
		player.inventory.append(self.item)

	def modify_player(self, player):
		if not self.isVisited:
			self.add_item(player)
			self.isVisited = True

class ItemsRoom(MapTile):
	def __init__(self, x, y, items):
		self.items = items
		MapTile.__init__(self, x, y)

	def add_item(self, player):
		for item in self.items:
			player.inventory.append(item)

	def modify_player(self, player):
		if not self.isVisited:
			self.add_item(player)
			self.isVisited = True

class LivingRoom(ItemRoom):
	def __init__(self, x, y):
		ItemRoom.__init__(self, x, y, items.Potato())

	def intro_text(self):
		if self.isVisited:
			return """
			Description here.
			"""
		else:
			return """
			Description here.
			"""

	def available_actions(self, player):
		super_actions = ItemRoom.available_actions(self, player)
		if self.item.state == "raw":
			super_actions.append(actions.CookPotato())
		return super_actions

class Bedroom(ItemRoom):
	def __init__(self, x, y):
		ItemRoom.__init__(self, x, y, items.MinnaHair())
		self.dirty = True

	def intro_text(self):
		if not self.isVisited:
			return """
			Description here.		
			"""
		else:
			return """
			Description here.
			"""

	def available_actions(self, player):
		super_actions = ItemRoom.available_actions(self, player)
		if self.dirty:
			super_actions.append(actions.DoLaundry())
		return super_actions


class Work(MapTile):
	def __init__(self, x, y):
		MapTile.__init__(self, x, y)

	def intro_text(self):
		return """
		Description here.
		"""

	def available_actions(self, player):
		super_actions = MapTile.available_actions(self, player)
		super_actions.append(actions.EnterWork())
		return super_actions


class Office(ItemsRoom):
	def __init__(self, x, y):
		room_items = [items.Dollar(), items.Dollar(), items.PuzzleClueTwo()]
		ItemsRoom.__init__(self, x, y, room_items)

	def intro_text(self):
		if not self.isVisited:
			return """
			Description here.
			"""
		else:
			return """
			Stop working, Rill.
			"""

	def modify_player(self, player):
		player.states.append("second_note")
		ItemsRoom.modify_player(self, player)
		
	def available_actions(self, player):
		super_actions = ItemsRoom.available_actions(self, player)
		super_actions.append(actions.LeaveWork())
		return super_actions


class FireBender(MapTile):
	def __init__(self, x, y):
		MapTile.__init__(self, x, y)


	def intro_text(self):
		return """
		Description here.
		"""

	def available_actions(self, player):
		super_actions = MapTile.available_actions(self, player)
		super_actions.append(actions.GetDrunk())
		return super_actions

class Hawthorne(MapTile):
	def __init__(self, x, y):
		MapTile.__init__(self, x, y)

	def intro_text(self):
		return """
		Description here.
		"""

	def available_actions(self, player):
		super_actions = MapTile.available_actions(self, player)
		super_actions.append(actions.DialPhone())
		return super_actions

class Nothing(MapTile):
	def __init__(self, x, y):
		MapTile.__init__(self, x, y)

	def intro_text(self):
		return """
		Nothing here.
		"""

class TextCorridor(MapTile):
	def __init__(self, x, y):
		MapTile.__init__(self, x, y)

	def intro_text(self):
		if not self.isVisited:
			return """
			Description here.
			"""
		else:
			return """
			Nothing here.
			"""

class BaseballCorridor(ItemRoom):
	def __init__(self, x, y):
		ItemRoom.__init__(self, x, y, items.Baseball())

	def intro_text(self):
		if not self.isVisited:
			return """
			Description here.
			"""
		else:
			return """
			Nothing here.
			"""

class Four09(MapTile):
	def __init__(self, x, y):
		MapTile.__init__(self, x, y)

	def intro_text(self):
		return """ 
		Description here.		
		"""
	
	def available_actions(self, player):
		super_actions = MapTile.available_actions(self, player)
		super_actions.append(actions.Play())
		super_actions.append(actions.LeaveApt())
		return super_actions


class MinnaHome(MapTile):
	def __init__(self, x, y):
		MapTile.__init__(self, x, y)

	def intro_text(self):
		return """
		Description here.
		"""

	def available_actions(self, player):
		super_actions = MapTile.available_actions(self, player)
		super_actions.append(actions.Solve())
		return super_actions

