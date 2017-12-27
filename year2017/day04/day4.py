with open('input.txt') as f:
    lines = f.readlines()

valid = len(lines)
for line in lines:
    phrases = line.strip('\n').split(" ")
    phrases.sort()
    index = 1
    while index < len(phrases):
        if phrases[index] == phrases[index -1]:
            valid = valid -1
            index = len(phrases)
        index += 1

print (valid)