import re
line = []
text = input()
while text:
    line.append(text)
    text = input()

final_string = ' '.join(line)
pattern = r"\d+"
result = re.findall(pattern, final_string)
print(*result)
