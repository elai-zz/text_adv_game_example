import world
from player import Player
	

def play():
	world.setup()
	player = Player()

	print """
	This is a text adveture game."""

	room = world.tile_exists(player.location_x, player.location_y)
	print(room.intro_text())
	while not player.victory:
		room = world.tile_exists(player.location_x, player.location_y)
		room.modify_player(player)
		available_actions = room.available_actions(player)

		print "Here are your available actions in this room:"
		for action in available_actions:
			print(action)
		print

		action_input = raw_input('Action: ')
		valid_action = False
		for action in available_actions:
			if action_input == action.name:
				valid_action = action
		if valid_action:
			player.room = room	
			player.do_action(valid_action, **action.kwargs)
		else:
			print "I didn't get that, please try again."

if __name__ == "__main__":
	play()