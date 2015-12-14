from Calculators.Artifact import Artifact
from Calculators.SansArtifact import SansArtifact

print("Destiny Light Calculator! Base on math by u/FluxDipole")
a = Artifact()
b = SansArtifact()
x = str(raw_input("Do you have an artifact?"))
if x.lower() == "yes":
    print("Using artifact in calculation...")
    armor_light = []
    weapon_light = []
    class_light = []
    for m in range(4):
        armor_light.append(int(raw_input("Enter your armor light")))
    for n in range(3):
        weapon_light.append(int(raw_input("Enter your weapon light")))
    for n in range(3):
        class_light.append(int(raw_input("Enter your class item, ghost, and artifact light")))
    a.armor(armor_light)
    a.classItems(class_light)
    a.weapons(weapon_light)
    print(a.lightTotal)
else:
    print("Artifact removed from calculation...")
    armor_light = []
    weapon_light = []
    class_light = []
    for m in range(4):
        armor_light.append(int(raw_input("Enter your armor light, 1 by 1")))
    for n in range(3):
        weapon_light.append(int(raw_input("Enter your weapon light, 1 by 1")))
    for n in range(2):
        class_light.append(int(raw_input("Enter your class item and ghost light, 1 by 1")))
    b.armor(armor_light)
    b.classItems(class_light)
    b.weapons(weapon_light)
    print(b.lightTotal)