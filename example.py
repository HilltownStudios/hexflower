from random import randrange
from hex_flower.flower import TerrainFlower

# Now use it
flower = TerrainFlower()

current_hex = flower.get_hex_by_id(1)
print(current_hex.id, current_hex.type)
for i in range(10):    
    d1 = randrange(1,6)
    d2 = randrange(1,6)
    
    roll = d1 + d2
    print(roll)
    next_hex = current_hex.get_next(roll)["hex"]
    current_hex = next_hex
    print(current_hex.id, current_hex.type)