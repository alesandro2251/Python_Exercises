# On the first line of the input, you will receive the encrypted message. After that, until the "Decode" command is 
# given, you will be receiving strings with instructions for different operations that need to be performed upon the 
# concealed message to interpret it and reveal its true content. There are several types of instructions, split by '|' 
# 
# · "Move {number of letters}":
# 
# o Moves the first n letters to the back of the string
# 
# · "Insert {index} {value}":
# 
# o Inserts the given value before the given index in the string
# 
# · "ChangeAll {substring} {replacement}":
# 
# o Changes all occurrences of the given substring with the replacement text


message = str(input())
encrypted_message = []

for letter in message:
    encrypted_message.append(letter)

break_flag = True
while break_flag:

    command = input().split("|")

    if command[0] == "Move":
        n_letters = encrypted_message[0:(int(command[1]))]
        for i in n_letters:
            encrypted_message.remove(i)
        for i in n_letters:
            encrypted_message.append(i)
    elif command[0] == "Insert":
        at = int(command[1])
        char = command[2]
        encrypted_message.insert(at, char)
    elif command[0] == "ChangeAll":
        change = command[1]
        to = command[2]
        for i in range(len(encrypted_message)):
            if encrypted_message[i] == change:
                encrypted_message[i] = to
    elif command[0] == "Decode":
        break_flag = False

print(f"The decrypted message is: {''.join(encrypted_message)}")

# zzHe

# ChangeAll|z|l

# Insert|2|o

# Move|3

# Decode
