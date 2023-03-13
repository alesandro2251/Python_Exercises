str = str(input()).split(" ")
dict = {}

for word in str:
    for i in word:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

for key in dict:
    print(f"{key} -> {dict[key]}")
