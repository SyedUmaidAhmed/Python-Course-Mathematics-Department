# 2-D List of planets
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]

flatten_planets = []

for sublist in planets:
	for planet in sublist:
		
		if len(planet) < 6:
			flatten_planets.append(planet)
		
print(flatten_planets)
