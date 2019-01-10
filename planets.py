planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.extend(["Uranus", "Neptune"])

planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")

planet_list.append("Pluto")

rocky_planets = planet_list[0:4]

# Delete pluto since its a dwarf planet :(
# del planet_list[-1]

spacecraft_visits = [
    ('Pioneer 10', 'Jupiter'),
    ('Pioneer 11', 'Jupiter', 'Saturn'),
    ('Voyager 1', 'Jupiter', 'Saturn'),
    ('Voyager 2', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'),
    ('Galileo', 'Jupiter'),
    ('Ulysses', 'Jupiter'),
    ('Cassini-Huygens', 'Jupiter', 'Saturn'),
    ('New Horizons', 'Jupiter', 'Pluto'),
    ('Juno', 'Jupiter'),
    ('Jupiter Icy Moons Explorer', 'Jupiter'),
    ('Europa Clipper', 'Jupiter')
]

print('Spacecraft Visits')
for planet in planet_list:
    print()
    print(f"----------{planet}----------")
    for visit in spacecraft_visits:
        if planet in visit:
            print(visit[0])