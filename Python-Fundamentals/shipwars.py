# Create a program that tracks the battle and either chooses a winner or prints a stalemate. On the first line, 
# you will receive the status of the pirate ship, which is a string representing integer sections separated by ">". 
# On the second line, you will receive the same type of status, but for the warship: 
 
# On the third line, you will receive the maximum health capacity a section of the ship can reach.
# 
# The following lines represent commands until "Retire":
# 
# · "Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section. Check if the
# index is valid and if not, skip the command. If the section breaks (health <= 0) the warship sinks, 
# print the following and stop the program: "You won! The enemy ship has sunken." 
# 
# · "Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that 
# range (indexes are inclusive). Check if both indexes are valid and if not, skip the command. If the section breaks 
# (health <= 0) the pirate ship sinks, print the following and stop the program: 
# 
# "You lost! The pirate ship has sunken."
# 
# · "Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health. Check if the 
# index is valid and if not, skip the command. The health of the section cannot exceed the maximum health capacity. 
# 
# · "Status" - prints the count of all sections of the pirate ship that need repair soon, which are all sections that
# are lower than 20% of the maximum health capacity. Print the following: 
# 
# "{count} sections need repair."
# 
# In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, 
# in the following format: 
# 
# "Pirate ship status: {pirateShipSum}
# 
# Warship status: {warshipSum}"
# 
# 4. Input
# 
# · On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
# 
# · On the 2nd line, you are going to receive the status of the warship
# 
# · On the 3rd line, you will receive the maximum health a section of a ship can reach.
# 
# · On the following lines, until "Retire", you will be receiving commands.

pirateShip = str(input()).split(">")
warShip = str(input()).split(">")
maxHealth = int(input())
count = 0
commands = ''
break_flag = False
pirateShipSum = 0
warShipSum = 0

while True:
    commands = str(input()).split(" ")

    if "Retire" in commands and 1 <= maxHealth <= 1000:
        break

    if commands[0] == 'Fire' and -200 <= int(commands[1]) <= 200 and int(commands[1]) <= len(warShip) and 1 <= int(
            commands[2]) <= 1000:
        index = int(commands[1])
        warShip[index] = int(warShip[index]) - int(commands[2])
        if int(warShip[index]) <= 0:
            print("You won! The enemy ship has sunken.")
            break
    elif commands[0] == 'Defend' and -200 <= int(commands[1]) <= 200 and -200 <= int(commands[2]) <= 200 and int(
            commands[1]) <= len(pirateShip) and int(commands[2]) <= len(pirateShip) and 1 <= int(commands[3]) <= 1000:
        indexStart = int(commands[1])
        indexEnd = int(commands[2]) + 1
        for i in range(len(pirateShip[indexStart:indexEnd])):
            pirateShip[i] = int(pirateShip[i]) - int(commands[3])
            if int(pirateShip[i]) <= 0:
                break_flag = True
                print("You lost! The pirate ship has sunken.")
                break
    elif commands[0] == 'Repair' and -200 <= int(commands[1]) <= 200 and int(commands[1]) <= len(warShip) and 1 <= int(
            commands[2]) <= 1000:
        index = int(commands[1])
        pirateShip[index] = int(pirateShip[index]) + int(commands[2])
        if int(pirateShip[index]) > maxHealth:
            pirateShip[index] = maxHealth
    elif commands[0] == 'Status':
        for i in range(len(pirateShip)):
            if int(pirateShip[i]) < ((maxHealth / 100) * 20):
                count += 1
        print(f"{count} sections need repair.")
        count = 0
    if break_flag:
        break

if not break_flag:
    for i in range(len(pirateShip)):
        pirateShipSum = pirateShipSum + int(pirateShip[i])

    for i in range(len(warShip)):
        warShipSum = warShipSum + int(warShip[i])

    print(f"Pirate ship status: {pirateShipSum}")
    print(f"Warship status: {warShipSum}")
