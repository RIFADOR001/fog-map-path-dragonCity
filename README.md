# fog-map-path-dragonCity
Dragoncity is a mobile game about dragon breedings and battles. It includes several
mini-games. One of them is fog map. Every cell has a different cost to visit for
first time, and the cost becomes 5 afterwards. The goal is to unlock as many important
items (goals) with the available points. 

This program recieves a map (in map.py) and the starting points and goals to
identify the best path starting on the start and passing through every goal (in the
given order).

The next step is use web scrapping to automatically download the map of the current event,
and maybe even use selenium to use a "path constructor" (tool in web to generate your own
path manually and verify the cost of that map. Then the map can be shared with others).