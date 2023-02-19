loot = str(input()).split("|")
stolen = []
allItemsL = 0

while True:
    commands = str(input()).split(" ")

    if "Yohoho!" in commands:
        break

    if commands[0] == "Loot":
        for i in range(1, len(commands)):
            if not commands[i] in loot:
                loot.insert(0, commands[i])
    elif commands[0] == "Drop" and -200 <= int(commands[1]) <= 200:
        index = int(commands[1])
        if index <= len(loot):
            x = loot[index]
            loot.remove(x)
            loot.append(x)
    elif commands[0] == "Steal" and 1 <= int(commands[1]) <= 100:
        count = int(commands[1])
        i = 0

        if count > len(loot):
            count = len(loot)

        for i in range(-1, (count * -1) + -1, -1):
            x = loot[-1]
            loot.remove(x)
            stolen.insert(0, x)

        print(", ".join(stolen))


if len(loot) == 0:
    print("Failed treasure hunt.")
else:
    for i in range(len(loot)):
        item = int(len(loot[i]))
        allItemsL += item

    averageGain = allItemsL / len(loot)
    print(f"Average treasure gain: {averageGain:.2f} pirate credits.")
