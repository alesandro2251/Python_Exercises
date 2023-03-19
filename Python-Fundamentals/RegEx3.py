import re
text = input()
word = input()
count = 0

pattern = fr'{word}\b'
result = re.findall(pattern, text, re.IGNORECASE)
print(len(result))
