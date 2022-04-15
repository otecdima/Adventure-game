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

## Lab 4.6

It is the new game, that contain two modeles, as the previous one. In that game I used classes and their methods, inheritance. The module `game.py` contains a few classes to run the game successfully, each of which has many additional methods. The module `main.py` is the main one for the game where there are the main cycle while of the game and part for creating game space

Plot: you are Ukrainian soldier that have the goal to kill putin. Your adventure will be occuring in a few cities/towns: Chornobaivka, Stryi, Lviv, Odesa, Kyiv, moskwa. At each city there are new weapons to defeat the next city/town enemy.

```
Welcome to my game!
You have a few locations, where there are weapons and enemies.
Your main goal to kill putin.
To win the game you should defeat all the enemies.
Good luck!

[Lera]: Hello, don't be afraid, I'm your friend!
My gift is in your backpack.


Stryi
--------------------
A beautiful town that has its long history.
The Lviv is north

Lera is here!
A girl with help
-----------
Choose the command:
- [north, south, east, west]: to move in chosen direction
- talk: to talk with the character
- fight: to fight with the enemy
- take: to take the item
- show: to show the items in backpack
-----------
>
```

Here is the start of the game. The part after Lera's phrase is the main cycle of the game, which have 5 commands to execute. Their description is above. The information below the name of teh city contain other directions to go, name and description of the charcter is there is any and the name and the description of the item if there is any.
