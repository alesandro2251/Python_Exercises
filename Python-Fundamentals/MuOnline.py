# You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's rooms. 
# Each room is separated with '|' (vertical bar): "room1|room2|room3…" 
# 
# Each room contains a command and a number, separated by space. The command can be:
# 
# · "potion"
# 
# o You are healed with the number in the second part. But your health cannot exceed your initial health (100).
# 
# o First print: "You healed for {amount} hp."
# 
# o After that, print your current health: "Current health: {health} hp."
# 
# · "chest"
# 
# o You've found some bitcoins, the number in the second part.
# 
# o Print: "You found {amount} bitcoins."
# 
# · In any other case, you are facing a monster, which you will fight. The second part of the room contains the 
# attack of the monster. You should remove the monster's attack from your health. 
# 
# o If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
# 
# o If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room you've manage 
# to reach: "Best room: {room}" 
# 
# If you managed to go through all the rooms in the dungeon, print on the following three lines:
# 
# "You've made it!"
# 
# "Bitcoins: {bitcoins}"
# 
# "Health: {health}"

rooms = str(input()).split("|")
health = 100
bitcoins = 0

break_flag = False

for i in range(len(rooms)):
    words = rooms[i].split(" ")

    if "chest" in words:
        bitcoins += int(words[1])
        print(f"You found {words[1]} bitcoins.")
    elif "potion" in words:
        health += int(words[1])
        if health >= 100:
            print(f"You healed for {int(words[1]) - (health - 100)} hp.")
            health = 100
        else:
            print(f"You healed for {words[1]} hp.")
        print(f"Current health: {health} hp.")
    else:
        monster = words[0]
        attack = int(words[1])
        health -= attack
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {i + 1}")
            break_flag = True

    if break_flag:
        break

if health > 0 and break_flag == False:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
