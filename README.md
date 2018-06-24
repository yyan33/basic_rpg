###Summary
Work in progress basic text RPG. Currently getting functions working before bothering with balancing gameplay. Adding features consistently to better familiarize myself with Python and OO programming in general. It is far from ideal, as I am learning as I go. I am also going for minimal use of outside packages.

###Current Features
#####Characters
* Player/Monster characters with class-dependant stats
* Functional battle stats (hp, phys atk, mag def, etc)
* Players can equip stat-modifying equipment
* Character and equipment stats stored and loaded from local SQLite database
#####World
* Start, End, Monster, and Empty Rooms
* Monster Rooms possess a monster of chosen strength for the player to defeat
* Empty Rooms are purely for dialogue/atmosphere
* Every Room has an entry text
* Loot (weapons/armor) can optionally be contained in either type of room
* Generate and populate map from local csv file
#####Gameplay
* Players can navigate through the map between rooms
* Players can battle monsters
* Battles are turn-based and use simple attack and defense stats
* Character rolls a 20-sided die and adds their (phys/mag) attack stat. A hit lands if the result is greater than the target's corresponding defense
* Damage is dependent on type of attack and enemy defense

### Potential Upcoming Features
#####Characters
* Add more complex stats (elemental resistances, class-specific equipmet, etc)
* Add spells & abilities with unique effects
* Add level progression
#####World
* Add flag for room that has already been entered
* Allow for procedurally generated maps: give dimensions and generate a csv with a connected path of rooms from start to end
* Procedurally generated rooms with random monsters & loot