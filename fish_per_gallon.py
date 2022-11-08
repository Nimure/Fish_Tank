# Tank Size in Gallons
tank_size = 55

# fish size in inches
fish = [["cardinal tetra" , int(1.5) ] , ["dwarf gourami", int(3.5) ] , ["discus" , 6]]

fish_size = [i[1] for i in fish]

# check fish_size list
print (fish_size)

# number of each type of fish
num = [10, 4, 3]

# rule of thumb is one inch of fish per gallon. So # of gallons = max fish inches

total_fish_size = []
for n1, n2 in zip(fish_size, num):
    total_fish_size.append(n1 * n2)

#tests above list multiplication
print(total_fish_size)

# turn the total_fish_size list into a single integer
fish_inches = sum(total_fish_size)

#test fish_inches
print(fish_inches)

def fish_per_gallon(fish_inches, tank_size):
    if ((fish_inches) <= (tank_size)):
        print("You have room for " + str((tank_size) - (fish_inches)) + " more inches of fish!")

    else:
        print("You cannot fit anymore fish!")

fish_per_gallon(fish_inches, tank_size)