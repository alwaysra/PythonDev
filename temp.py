sd=[
    [0,2,0,4,0,9,1,0,0],
    [0,0,6,0,5,0,0,8,9],
    [0,7,0,0,8,3,0,2,4],
    [7,1,0,5,0,0,0,0,0],
    [0,0,0,0,9,0,2,0,0],
    [0,0,0,0,4,0,0,0,7],
    [0,6,0,0,0,0,0,0,0],
    [0,0,7,3,0,0,8,0,1],
    [3,4,0,0,0,5,0,6,0]
]
xgg0=[];xgg1=[];xgg2=[];xgg3=[];xgg4=[];xgg5=[];xgg6=[];xgg7=[];xgg8=[];

def xgg():
    for x in range(3):
        for y in range(3):
            if x//3==0 | y//3==0:
                if sd[x][y]!=0:
                    xgg0.append(sd[x][y])
    for x in range(3):
        for y in range(3,6):
            if sd[x][y]!=0:
                xgg1.append(sd[x][y])
    for x in range(3):
        for y in range(6,9):
            if sd[x][y]!=0:
                xgg2.append(sd[x][y])
    for x in range(3,6):
        for y in range(3):
            if sd[x][y] != 0:
                xgg3.append(sd[x][y])
    for x in range(3,6):
        for y in range(3,6):
            if sd[x][y] != 0:
                xgg4.append(sd[x][y])
    for x in range(3,6):
        for y in range(6,9):
            if sd[x][y] != 0:
                xgg5.append(sd[x][y])
    for x in range(6,9):
        for y in range(3):
            if sd[x][y] != 0:
                xgg6.append(sd[x][y])
    for x in range(6,9):
        for y in range(3,6):
            if sd[x][y] != 0:
                xgg7.append(sd[x][y])
    for x in range(6,9):
        for y in range(6,9):
            if sd[x][y] != 0:
                xgg8.append(sd[x][y])
    print(xgg0)
    print(xgg1)
    print(xgg2)
    print(xgg3)
    print(xgg4)
    print(xgg5)
    print(xgg6)
    print(xgg7)
    print(xgg8)

print(sd)
sd[8][8]=2
print(sd)