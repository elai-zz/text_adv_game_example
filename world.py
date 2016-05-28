from maptile import *

_world = {}
starting_position = (3, 3)

def tile_exists(x, y):
    return _world.get((x, y))

def setup():
	_world[(3, 0)] = Nothing(3, 0)
	_world[(3, 1)] = TextCorridor(3, 1)
	_world[(3, 2)] = Nothing(3, 2)
	_world[(3, 3)] = Bedroom(3, 3)
	_world[(3, 4)] = LivingRoom(3, 4)
	_world[(3, 5)] = Nothing(3, 5)

	_world[(2, 0)] = Nothing(2, 0)

	_world[(1, 0)] = Nothing(1, 0)
	_world[(0, 0)] = FireBender(0, 0)
	_world[(0, 1)] = Nothing(0 ,1)
	_world[(0, 2)] = Work(0, 2)

	_world[(4, 1)] = Nothing(4, 1)
	_world[(5, 1)] = BaseballCorridor(5, 1)
	_world[(5, 0)] = Hawthorne(5, 0)
	_world[(4, 5)] = Nothing(4, 5)
	_world[(5, 5)] = MinnaHome(5, 5)

	_world[(20, 20)] = Four09(20, 20)
	_world[(10, 10)] = Office(10, 10)