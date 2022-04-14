# Wanderer-games

## Lab 4.5

The module of the game from that task was made with the help of the module `main.py` and with example of the game's realization from the txt. The module `game.py` contains a few classes to run the game successfully, each of which has many additional methods. 

Classes:
- `Room`
- `Enemy`
- `Item`

The game runs with the help of the second module `main.py`, which conditionally is divided into two parts. The first one allows you to create a game space, and the second is main game cycle.

The second part contains such commands:
- north, south, east, west – move the character to the certain direction.
- talk – converstion with the enemy, the one gives the phrase to start converstion, however in one side :(
- fight - fight with the enemy
- take - takes the item
