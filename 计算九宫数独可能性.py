sd=[
    [0,1,0,3,0,9,0,6,0],
    [9,0,0,5,1,6,0,0,2],
    [0,0,5,0,0,0,9,0,0],
    [1,7,0,0,4,0,0,9,5],
    [0,5,0,7,0,3,0,2,0],
    [2,9,0,0,5,0,0,7,6],
    [0,0,6,0,0,0,2,0,0],
    [7,0,0,1,8,5,0,0,3],
    [0,3,0,2,0,4,0,5,0]
]
sd=[
    [0,6,0,0,1,0,0,7,0],
    [8,0,1,0,0,0,0,0,2],
    [0,0,0,5,2,0,0,1,0],
    [0,0,0,3,0,9,1,0,6],
    [4,0,3,0,0,0,5,0,8],
    [6,0,5,2,0,8,0,0,0],
    [0,4,0,0,3,5,0,0,0],
    [1,0,0,0,0,0,3,0,9],
    [0,3,0,0,9,0,0,8,0]
]
caicezidian={}
xgg0=[];xgg1=[];xgg2=[];xgg3=[];xgg4=[];xgg5=[];xgg6=[];xgg7=[];xgg8=[]
#查找所有空白单元格 并且生成字典
def findnull():
    for x in range(9):
        for y in range(9):
            if sd[x][y]==0:
                caicezidian[str(x)+str(y)]=[1,2,3,4,5,6,7,8,9]
                xgg()
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
    a()

#将猜测字典的每个获得坐标点并且给过滤器
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

#过滤器 将输入的坐标点每列比较 每行比较 然后刷新猜测字典
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
    #print("xyXY轴和小宫格可能性:" + x + y + str(lia))
    caicezidian[str(int(x))+str(int(y))]=lia
    checkonly(x,y)

#检查唯一性 如果猜测字典中只有一个将这个数字填写到对应数独坐标中 然后查找所有空白单元格
def checkonly(x,y):
    vs=list(caicezidian.values())
    for i in range(len(vs)):
        if len(vs[i])==1:
            #只有一个可能性就将这个可能性填写到数独中
            print(str(int(x))+str(int(y))+"-"+str(caicezidian[str(int(x))+str(int(y))][0]))
            sd[int(x)][int(y)]=(caicezidian[str(int(x))+str(int(y))][0])
            caicezidian.pop(str(int(x))+str(int(y)))


#填写最大的值
def fillmax():
    print("fillmax_start")
    zbs=list(caicezidian.keys())
    vs = list(caicezidian.values())
    for i in range(len(zbs)):
        x=zbs[i][0]
        y=zbs[i][1]
        for i in range(len(vs)):
            sd[int(x)][int(y)] = (max(vs[i]))

if __name__ == '__main__':
        print(sd)
        findnull()
        while True:
            if len(caicezidian)==0:
                print("解题成功")
                for i in range(9):
                    print(sd[i])
                break
            else:
                print("还有"+str(len(caicezidian))+"个字典列表")
                findnull()
                print(caicezidian)