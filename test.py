# This space is just for review  exercises.
#

captains = {
    "Enterprise": "Picard",
    "Voyager": "Janeway",
    "Defiant": "Sisko"
}

if 'Enterprise' in captains:
    print("It's there")

if "Discovery" in captains:
    print("It's there")
else:
    captains['Discovery'] = 'unknown'
    print(captains['Discovery'])

for ship in captains:
    print(f"The {ship} is captained by {captains[ship]}")

del captains["Discovery"]
print(captains)