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
caicezidian={}
xgg0=[];xgg1=[];xgg2=[];xgg3=[];xgg4=[];xgg5=[];xgg6=[];xgg7=[];xgg8=[]
#查找所有空白 并且生成字典
def findnull():
    for x in range(9):
        for y in range(9):
            if sd[x][y]==0:
                caicezidian[str(x)+str(y)]=[1,2,3,4,5,6,7,8,9]
#过滤所有坐标点 然后计算可能性

#得到所有小宫格的数值
def xgg():
    for x in range(3):
        for y in range(3):
            if x // 3 == 0 | y // 3 == 0:
                if sd[x][y] != 0:
                    xgg0.append(sd[x][y])
    for x in range(3):
        for y in range(3, 6):
            if sd[x][y] != 0:
                xgg1.append(sd[x][y])
    for x in range(3):
        for y in range(6, 9):
            if sd[x][y] != 0:
                xgg2.append(sd[x][y])
    for x in range(3, 6):
        for y in range(3):
            if sd[x][y] != 0:
                xgg3.append(sd[x][y])
    for x in range(3, 6):
        for y in range(3, 6):
            if sd[x][y] != 0:
                xgg4.append(sd[x][y])
    for x in range(3, 6):
        for y in range(6, 9):
            if sd[x][y] != 0:
                xgg5.append(sd[x][y])
    for x in range(6, 9):
        for y in range(3):
            if sd[x][y] != 0:
                xgg6.append(sd[x][y])
    for x in range(6, 9):
        for y in range(3, 6):
            if sd[x][y] != 0:
                xgg7.append(sd[x][y])
    for x in range(6, 9):
        for y in range(6, 9):
            if sd[x][y] != 0:
                xgg8.append(sd[x][y])

def a():
    zbs=list(caicezidian.keys())
    for i in range(len(zbs)):
        x=zbs[i][0]
        y=zbs[i][1]
        #根据坐标的XY计算在第几个宫格
        if str(int(x)//3)+str(int(y)//3)=='00':
            ggno=0
        elif str(int(x)//3)+str(int(y)//3)=='01':
            ggno = 1
        elif str(int(x)//3)+str(int(y)//3)=='02':
            ggno = 2
        elif str(int(x)//3)+str(int(y)//3)=='10':
            ggno = 3
        elif str(int(x)//3)+str(int(y)//3)=='11':
            ggno = 4
        elif str(int(x)//3)+str(int(y)//3)=='12':
            ggno = 5
        elif str(int(x)//3)+str(int(y)//3)=='20':
            ggno = 6
        elif str(int(x)//3)+str(int(y)//3)=='21':
            ggno = 7
        else:
            ggno=8
        guolv(x,y,ggno)

def guolv(x,y,ggno):
    #print("xy:" + x + y)
    lia=list(caicezidian[x+y])#
    lib=list(sd[int(x)])#得到数独第x列
    for i in lib:
        if i in lia:
            lia.remove(i)
    #print("xyY轴可能性:"+x+y+str(lib))
    lic=[]
    for i in range(9):
        if sd[int(i)][int(y)]!=0:
            lic.append(sd[int(i)][int(y)])
    #print(lic)
    for j in lic:
        if j in lia:
            lia.remove(j)
    #print("xyXY轴可能性:"+x+y+str(lia))
    if ggno==0:
        for i in xgg0:
            if i in lia:
                lia.remove(i)
    if ggno==1:
        for i in xgg1:
            if i in lia:
                lia.remove(i)
    if ggno==2:
        for i in xgg2:
            if i in lia:
                lia.remove(i)
    if ggno==3:
        for i in xgg3:
            if i in lia:
                lia.remove(i)
    if ggno==4:
        for i in xgg4:
            if i in lia:
                lia.remove(i)
    if ggno==5:
        for i in xgg5:
            if i in lia:
                lia.remove(i)
    if ggno==6:
        for i in xgg6:
            if i in lia:
                lia.remove(i)
    if ggno==7:
        for i in xgg7:
            if i in lia:
                lia.remove(i)
    if ggno==8:
        for i in xgg8:
            if i in lia:
                lia.remove(i)
    print("xyXY轴和小宫格可能性:" + x + y + str(lia))

if __name__ == '__main__':
    findnull()
    xgg()
    a()