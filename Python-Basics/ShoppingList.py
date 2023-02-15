# You will receive an initial list with groceries separated by an exclamation mark "!".
# 
# After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
# 
# · "Urgent {item}" - add the item at the start of the list. If the item already exists, skip this command.
# 
# · "Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, 
# skip this command. 
# 
# · "Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one. 
# Otherwise, skip this command. 
# 
# · "Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the end
# of the list. Otherwise, skip this command. 

result = []
start = str(input()).split('!')

for i in range(len(start)):
    result.append(start[i])
word = ''

while True:
    word = str(input()).split(' ')
    if "Shopping!" in word:
        break
    else:
        if word[0] == 'Urgent' and not word[1] in result:
            result.insert(0, word[1])
        elif word[0] == "Unnecessary" and word[1] in result:
            result.remove(word[1])
        elif word[0] == "Correct" and word[1] in result:
            for i in range(len(result)):
                if result[i] == word[1]:
                    result.remove(word[1])
                    result.insert(i, word[2])
        elif word[0] == "Rearrange" and word[1] in result:
            result.remove(word[1])
            result.append(word[1])

print(", ".join(result))
