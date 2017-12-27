count = 1
total = 1
result = 289326
result2 = 289326

xpos = 0
ypos = 0
dx = 1
dy = 1
while total < result:
    mx = 0
    while mx < count and total < result:
        xpos += dx
        mx += 1
        total += 1
    my = 0
    while my < count and total < result:
        ypos += dy
        my += 1
        total += 1
    dx = dx * -1
    dy = dy * -1
    count += 1

print (total)
journey = abs(xpos) + abs(ypos)
print (journey)
