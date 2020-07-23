height = int(input())
string = "#"
pattern = []
for i in range(height):
    if i == 0:
        pattern.append(string)
    else:
        string += 2 * '#'
        pattern.append(string)
for i in range(len(pattern)):
    pattern[i] = pattern[i].center(len(pattern[height - 1]))
    print(pattern[i])


