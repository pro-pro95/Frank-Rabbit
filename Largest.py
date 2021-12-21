highest_building_so_far = 0
print ("The Tallest building so far is:", highest_building_so_far)
for building_height in [49, 58, 25, 69,35,78,51,78,78,32,90,500, 22, 5000,45]:
    if building_height > highest_building_so_far:
        highest_building_so_far = building_height
    print (building_height, highest_building_so_far)

print ("The Tallest building is:", highest_building_so_far)
