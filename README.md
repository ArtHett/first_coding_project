First big coding project. A 'rogue-like' with pokemon battle-mechanics, without any capture or creature training. 
You the hero will navigate dungeons with different monsters, events and secretes. While exploring and fighting,
you will collect items and learn abilities. Manage your health, ressources, items etc well and you might reach
the act boss and defeat him. When your life reaches 0 you have to start all over again (in good rogue-like fashion)
once act=3 is implemented, i aim for a typical run to be about 1 hour long (again in good RL fashion).

Already containing:
-minimum content for act1 and act2, 
-over 20 different enemies 
-over 40 items and consumables
-about 20 different abilities hero the can learn

enemy_sprites are made with chatGPT and Claude Opus 5.5, all icons in game are from the game classic 'WarCraft3'

[Kampfsystem](images/example_battle.png)
[Event](images/example_event.png)
[Dungeon](images/act2_start.png)

recommended is installing either Python3.12 or using venv to launch this script with 3.12
with terminal you have to move to the right directory and 'pip install pygame'
When i switched my game from console/text based to pygame, only Python 3.12 was feature complete
with pygame. With newer versions of python, pygame might not be supported

